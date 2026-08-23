import datetime
import json
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


def _now():
    return datetime.datetime.now(datetime.UTC).isoformat()


def _representative_priority(record):
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


def _select_representative(members):
    return max(members, key=_representative_priority)


def _group_members(conn, dedup_group_id):
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT
            nr.*,
            qr.query_label
        FROM dedup_group_members dgm
        JOIN normalized_records nr ON nr.record_id = dgm.record_id
        LEFT JOIN query_runs qr ON qr.query_run_id = nr.query_run_id
        WHERE dgm.dedup_group_id = ?
        ORDER BY dgm.is_representative_candidate DESC, nr.metadata_completeness_score DESC, nr.record_id ASC
        """,
        (dedup_group_id,),
    )
    return cursor.fetchall()


def _log_audit(conn, *, action_type, dedup_group_id=None, study_id=None, record_ids=None, previous_status=None, new_status=None, reason=None, reviewer_note=None):
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO dedup_audit_log (
            audit_id, timestamp, action_type, dedup_group_id, study_id,
            record_ids_json, previous_status, new_status, reason, reviewer_note
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        (
            str(uuid4()),
            _now(),
            action_type,
            dedup_group_id,
            study_id,
            json.dumps(record_ids or []),
            previous_status,
            new_status,
            reason,
            reviewer_note,
        ),
    )


def _create_unique_study(conn, members, *, dedup_group=None, new_status="merged", link_reason="deduplicated_match", reviewer_note=None):
    cursor = conn.cursor()
    representative = _select_representative(members)
    study_id = str(uuid4())
    timestamp = _now()
    source_databases = sorted({member["source_database"] for member in members if member["source_database"]})
    query_labels = sorted({member["query_label"] for member in members if member["query_label"]})
    query_run_ids = sorted({member["query_run_id"] for member in members if member["query_run_id"]})

    cursor.execute(
        """
        INSERT INTO unique_studies (
            study_id, representative_record_id, title, first_author, year, journal, doi, pmid, pmcid,
            abstract, publication_type, language, source_databases_json, query_labels_json,
            query_run_ids_json, linked_record_count, metadata_completeness_score, dedup_status,
            screening_status, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'not_started', ?, ?)
        """,
        (
            study_id,
            representative["record_id"],
            representative["title"],
            representative["first_author"],
            representative["year"],
            representative["journal"],
            representative["doi"],
            representative["pmid"],
            representative["pmcid"],
            representative["abstract"],
            representative["publication_type"],
            representative["language"],
            json.dumps(source_databases),
            json.dumps(query_labels),
            json.dumps(query_run_ids),
            len(members),
            representative["metadata_completeness_score"] or 0,
            new_status,
            timestamp,
            timestamp,
        ),
    )

    for member in members:
        cursor.execute(
            """
            INSERT OR REPLACE INTO unique_study_record_links (
                study_id, record_id, raw_record_id, query_run_id,
                source_database, query_label, link_reason, created_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                study_id,
                member["record_id"],
                member["raw_record_id"],
                member["query_run_id"],
                member["source_database"],
                member["query_label"],
                link_reason,
                timestamp,
            ),
        )

    if dedup_group:
        cursor.execute(
            """
            UPDATE dedup_groups
            SET status = ?, representative_record_id = ?, representative_study_id = ?, reviewed_at = ?, reviewer_note = ?
            WHERE dedup_group_id = ?
            """,
            (
                new_status,
                representative["record_id"],
                study_id,
                timestamp,
                reviewer_note,
                dedup_group["dedup_group_id"],
            ),
        )

    _log_audit(
        conn,
        action_type="create_unique_study" if not dedup_group else "merge_dedup_group",
        dedup_group_id=dedup_group["dedup_group_id"] if dedup_group else None,
        study_id=study_id,
        record_ids=[member["record_id"] for member in members],
        previous_status=dedup_group["status"] if dedup_group else None,
        new_status=new_status,
        reason=link_reason,
        reviewer_note=reviewer_note,
    )
    return study_id


def bulk_merge_exact(conn, group_ids=None, reviewer_note=None):
    """Merge exact duplicate groups into unique_studies while preserving provenance."""
    cursor = conn.cursor()
    params = []
    query = """
        SELECT *
        FROM dedup_groups
        WHERE match_type LIKE 'exact_%'
    """
    if group_ids:
        placeholders = ",".join("?" for _ in group_ids)
        query += f" AND dedup_group_id IN ({placeholders})"
        params.extend(group_ids)
    else:
        query += " AND status = 'auto_merge_ready'"
    cursor.execute(query, params)
    groups = cursor.fetchall()

    merged_count = 0
    for group in groups:
        members = _group_members(conn, group["dedup_group_id"])
        if not members:
            continue
        status = "merged_by_human" if group_ids else "merged"
        _create_unique_study(
            conn,
            members,
            dedup_group=group,
            new_status=status,
            link_reason=f"{group['match_type']}_group",
            reviewer_note=reviewer_note,
        )
        merged_count += 1

    conn.commit()
    return merged_count


def process_singletons(conn):
    """Create unique_studies for all records not linked through dedup groups."""
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT nr.*, qr.query_label
        FROM normalized_records nr
        LEFT JOIN unique_study_record_links usrl ON usrl.record_id = nr.record_id
        LEFT JOIN query_runs qr ON qr.query_run_id = nr.query_run_id
        WHERE usrl.record_id IS NULL
          AND nr.record_id NOT IN (
              SELECT dgm.record_id
              FROM dedup_group_members dgm
              JOIN dedup_groups dg ON dg.dedup_group_id = dgm.dedup_group_id
              WHERE dg.status IN ('pending', 'auto_merge_ready')
          )
        ORDER BY nr.created_at ASC, nr.record_id ASC
        """
    )
    singletons = cursor.fetchall()

    created = 0
    for record in singletons:
        _create_unique_study(conn, [record], new_status="singleton", link_reason="singleton_record")
        created += 1

    conn.commit()
    return created


def merge_group_manual(conn, group_id, notes=None):
    """Merge a specific pending or fuzzy dedup group with human confirmation."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dedup_groups WHERE dedup_group_id = ?", (group_id,))
    group = cursor.fetchone()
    if not group:
        return False

    members = _group_members(conn, group_id)
    if not members:
        return False

    _create_unique_study(
        conn,
        members,
        dedup_group=group,
        new_status="merged_by_human",
        link_reason=f"{group['match_type']}_manual_merge",
        reviewer_note=notes,
    )
    conn.commit()
    return True


def reject_group_manual(conn, group_id, notes=None, new_status="kept_separate"):
    """Mark a dedup group as reviewed without merging it."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dedup_groups WHERE dedup_group_id = ?", (group_id,))
    group = cursor.fetchone()
    if not group:
        return False

    cursor.execute(
        """
        UPDATE dedup_groups
        SET status = ?, reviewed_at = ?, reviewer_note = ?
        WHERE dedup_group_id = ?
        """,
        (new_status, _now(), notes, group_id),
    )
    cursor.execute(
        """
        SELECT record_id
        FROM dedup_group_members
        WHERE dedup_group_id = ?
        ORDER BY record_id
        """,
        (group_id,),
    )
    record_ids = [row["record_id"] for row in cursor.fetchall()]
    _log_audit(
        conn,
        action_type="review_dedup_group",
        dedup_group_id=group_id,
        record_ids=record_ids,
        previous_status=group["status"],
        new_status=new_status,
        reviewer_note=notes,
    )
    conn.commit()
    return True
