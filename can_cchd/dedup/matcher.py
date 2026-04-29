import datetime
import difflib
import re
from uuid import uuid4


SOURCE_PRIORITY = {
    "PubMed": 11,
    "Embase": 10,
    "Scopus": 9,
    "Web of Science": 8,
    "Europe PMC": 7,
    "SciELO": 6,
    "LILACS/BVS": 5,
    "Semantic Scholar": 4,
    "OpenAlex": 3,
    "Crossref": 2,
    "Google Scholar": 1,
}


def normalize_title(title):
    if not title:
        return ""
    title = title.lower()
    title = re.sub(r"[^\w\s]", "", title)
    return re.sub(r"\s+", " ", title).strip()


def normalize_author(author):
    if not author:
        return ""
    author = author.lower()
    author = re.sub(r"[^\w\s]", "", author)
    return re.sub(r"\s+", " ", author).strip()


def _now():
    return datetime.datetime.now(datetime.UTC).isoformat()


def _assert_qa_gate_passed(conn):
    """Blocks deduplication if collection QA gate has not passed."""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT status FROM collection_qa_gate WHERE gate_id = 'main'")
        row = cursor.fetchone()
        if not row:
            raise RuntimeError("Collection QA Gate has not been run. Run Phase 1 QA Gate before deduplication.")
        status = row["status"] if hasattr(row, "__getitem__") and isinstance(row, dict) else row[0]
        if status not in ("pass", "warn"):
            raise RuntimeError(
                f"Collection QA Gate status is '{status}'. "
                "Resolve blocking issues in Phase 1 QA Gate before proceeding."
            )
    except Exception as e:
        if "no such table" in str(e).lower():
            return
        raise


def _record_priority(record):
    return (
        record["metadata_completeness_score"] or 0,
        1 if record["abstract"] else 0,
        1 if record["pmid"] else 0,
        1 if record["doi"] else 0,
        1 if record["pmcid"] else 0,
        1 if record["journal"] else 0,
        1 if record["year"] else 0,
        SOURCE_PRIORITY.get(record["source_database"], 0),
        len(record["title"] or ""),
        len(record["abstract"] or ""),
    )


def _choose_representative(records):
    return max(records, key=_record_priority)


def _clear_groups(conn, match_types):
    cursor = conn.cursor()
    placeholders = ",".join("?" for _ in match_types)
    cursor.execute(
        f"""
        DELETE FROM dedup_group_members
        WHERE dedup_group_id IN (
            SELECT dedup_group_id
            FROM dedup_groups
            WHERE match_type IN ({placeholders})
              AND status IN ('pending', 'auto_merge_ready')
        )
        """,
        match_types,
    )
    cursor.execute(
        f"""
        DELETE FROM dedup_groups
        WHERE match_type IN ({placeholders})
          AND status IN ('pending', 'auto_merge_ready')
        """,
        match_types,
    )


def _fetch_candidate_records(conn, exclude_grouped=False):
    cursor = conn.cursor()
    exclusion = ""
    if exclude_grouped:
        exclusion = """
          AND nr.record_id NOT IN (
              SELECT dgm.record_id
              FROM dedup_group_members dgm
              JOIN dedup_groups dg ON dg.dedup_group_id = dgm.dedup_group_id
              WHERE dg.status IN ('pending', 'auto_merge_ready')
          )
        """
    cursor.execute(
        f"""
        SELECT
            nr.record_id,
            nr.raw_record_id,
            nr.query_run_id,
            nr.source_database,
            nr.title,
            nr.title_normalized,
            nr.first_author,
            nr.authors_raw,
            nr.year,
            nr.journal,
            nr.doi,
            nr.doi_normalized,
            nr.pmid,
            nr.pmcid,
            nr.abstract,
            nr.metadata_completeness_score,
            qr.query_label
        FROM normalized_records nr
        LEFT JOIN unique_study_record_links usrl ON usrl.record_id = nr.record_id
        LEFT JOIN query_runs qr ON qr.query_run_id = nr.query_run_id
        WHERE usrl.record_id IS NULL
        {exclusion}
        ORDER BY nr.created_at ASC, nr.record_id ASC
        """
    )
    return cursor.fetchall()


def _has_identifier_conflict(records, group_key_name):
    for field in ("pmid", "doi_normalized", "pmcid"):
        if field == group_key_name:
            continue
        values = {record[field] for record in records if record[field]}
        if len(values) > 1:
            return True
    return False


def _insert_group(conn, match_type, match_key, records, confidence, group_key_name):
    if len(records) < 2:
        return
    cursor = conn.cursor()
    representative = _choose_representative(records)
    dedup_group_id = str(uuid4())
    status = "auto_merge_ready" if not _has_identifier_conflict(records, group_key_name) and match_type != "fuzzy_title" else "pending"
    cursor.execute(
        """
        INSERT INTO dedup_groups (
            dedup_group_id, match_type, match_key, confidence, status,
            representative_record_id, created_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            dedup_group_id,
            match_type,
            match_key,
            confidence,
            status,
            representative["record_id"],
            _now(),
        ),
    )
    for record in records:
        cursor.execute(
            """
            INSERT INTO dedup_group_members (
                dedup_group_id, record_id, is_representative_candidate, source_database,
                query_run_id, query_label, pmid, doi, pmcid, title, year, journal,
                metadata_completeness_score
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                dedup_group_id,
                record["record_id"],
                1 if record["record_id"] == representative["record_id"] else 0,
                record["source_database"],
                record["query_run_id"],
                record["query_label"],
                record["pmid"],
                record["doi"],
                record["pmcid"],
                record["title"],
                record["year"],
                record["journal"],
                record["metadata_completeness_score"],
            ),
        )


def run_exact_matcher(conn):
    """Find exact duplicate groups from normalized_records."""
    _assert_qa_gate_passed(conn)
    exact_types = ["exact_pmid", "exact_doi", "exact_pmcid", "exact_title", "exact_title_author"]
    _clear_groups(conn, exact_types)

    records = _fetch_candidate_records(conn)
    by_pmid = {}
    by_doi = {}
    by_pmcid = {}
    by_title = {}
    by_title_author = {}

    for record in records:
        if record["pmid"]:
            by_pmid.setdefault(record["pmid"], []).append(record)
        if record["doi_normalized"]:
            by_doi.setdefault(record["doi_normalized"], []).append(record)
        if record["pmcid"]:
            by_pmcid.setdefault(record["pmcid"], []).append(record)

        title_normalized = record["title_normalized"] or normalize_title(record["title"])
        if len(title_normalized) >= 20:
            by_title.setdefault(title_normalized, []).append(record)
            author_key = normalize_author(record["first_author"])
            if author_key:
                by_title_author.setdefault(f"{title_normalized}|{author_key}", []).append(record)

    used_ids = set()

    def insert_priority_groups(group_map, match_type, confidence, group_key_name):
        for key, grouped in group_map.items():
            available = [record for record in grouped if record["record_id"] not in used_ids]
            if len(available) > 1:
                _insert_group(conn, match_type, key, available, confidence, group_key_name)
                used_ids.update(record["record_id"] for record in available)

    insert_priority_groups(by_pmid, "exact_pmid", 1.0, "pmid")
    insert_priority_groups(by_doi, "exact_doi", 1.0, "doi_normalized")
    insert_priority_groups(by_pmcid, "exact_pmcid", 1.0, "pmcid")
    insert_priority_groups(by_title, "exact_title", 0.99, "title_normalized")
    insert_priority_groups(by_title_author, "exact_title_author", 0.98, "title_normalized")

    conn.commit()


def _fuzzy_candidate(r1, r2, score):
    shared_identifier = any(
        r1[field] and r1[field] == r2[field]
        for field in ("pmid", "doi_normalized", "pmcid")
    )
    supportive_evidence = (
        normalize_author(r1["first_author"]) == normalize_author(r2["first_author"])
        or (r1["year"] and r2["year"] and r1["year"] == r2["year"])
        or shared_identifier
    )
    if score >= 0.97:
        return supportive_evidence
    if 0.90 <= score < 0.97:
        return supportive_evidence
    return False


def run_fuzzy_matcher(conn):
    """Find fuzzy title duplicate groups from normalized_records."""
    _assert_qa_gate_passed(conn)
    _clear_groups(conn, ["fuzzy_title"])
    records = _fetch_candidate_records(conn, exclude_grouped=True)

    matched = set()
    for index, record in enumerate(records):
        if record["record_id"] in matched:
            continue
        title_1 = record["title_normalized"] or normalize_title(record["title"])
        if len(title_1) < 20:
            continue
        members = [record]
        for other in records[index + 1:]:
            if other["record_id"] in matched:
                continue
            title_2 = other["title_normalized"] or normalize_title(other["title"])
            if len(title_2) < 20:
                continue
            score = difflib.SequenceMatcher(None, title_1, title_2).ratio()
            if _fuzzy_candidate(record, other, score):
                members.append(other)
        if len(members) > 1:
            _insert_group(conn, "fuzzy_title", title_1[:100], members, max(difflib.SequenceMatcher(None, title_1, normalize_title(m["title"])).ratio() for m in members[1:]), "title_normalized")
            matched.update(member["record_id"] for member in members)

    conn.commit()
