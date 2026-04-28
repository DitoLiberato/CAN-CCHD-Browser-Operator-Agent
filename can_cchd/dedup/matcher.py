import re
import difflib
from uuid import uuid4

def normalize_title(title):
    if not title: return ""
    title = title.lower()
    # Remove punctuation
    title = re.sub(r'[^\w\s]', '', title)
    # Remove extra spaces
    return re.sub(r'\s+', ' ', title).strip()

def _assert_qa_gate_passed(conn):
    """Blocks deduplication if collection QA gate has not passed."""
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT status FROM collection_qa_gate WHERE gate_id = 'main'")
        row = cursor.fetchone()
        if not row:
            raise RuntimeError("Collection QA Gate has not been run. Run Phase 1 QA Gate before deduplication.")
        status = row["status"] if hasattr(row, '__getitem__') and isinstance(row, dict) else row[0]
        if status not in ("pass", "warn"):
            raise RuntimeError(
                f"Collection QA Gate status is '{status}'. "
                "Resolve blocking issues in Phase 1 QA Gate before proceeding."
            )
    except Exception as e:
        if "no such table" in str(e).lower():
            # Old schema — allow dedup to proceed (backward compatibility)
            return
        raise


def run_exact_matcher(conn):
    """Finds exact duplicates and populates duplicate_groups."""
    _assert_qa_gate_passed(conn)
    cursor = conn.cursor()
    
    # 1. Clear existing unmerged exact groups
    cursor.execute("DELETE FROM duplicate_group_members WHERE group_id IN (SELECT group_id FROM duplicate_groups WHERE status = 'pending' AND match_type LIKE 'exact_%')")
    cursor.execute("DELETE FROM duplicate_groups WHERE status = 'pending' AND match_type LIKE 'exact_%'")
    
    # 2. Get all records not yet linked to a study
    cursor.execute("SELECT record_id, pmid, doi, pmcid, title, year FROM records WHERE record_id NOT IN (SELECT record_id FROM study_links)")
    records = cursor.fetchall()
    
    # Grouping dictionaries
    by_pmid = {}
    by_doi = {}
    by_pmcid = {}
    by_title_year = {}
    
    for r in records:
        if r["pmid"]: by_pmid.setdefault(r["pmid"], []).append(r["record_id"])
        if r["doi"]: by_doi.setdefault(r["doi"], []).append(r["record_id"])
        if r["pmcid"]: by_pmcid.setdefault(r["pmcid"], []).append(r["record_id"])
        
        norm_title = normalize_title(r["title"])
        if norm_title and r["year"]:
            key = f"{norm_title}|{r['year']}"
            by_title_year.setdefault(key, []).append(r["record_id"])
            
    # Helper to insert groups
    def insert_groups(group_dict, match_type):
        for key, rec_ids in group_dict.items():
            if len(rec_ids) > 1:
                group_id = str(uuid4())
                cursor.execute(
                    "INSERT INTO duplicate_groups (group_id, match_type, match_key, status) VALUES (?, ?, ?, 'pending')",
                    (group_id, match_type, key)
                )
                for rid in rec_ids:
                    cursor.execute(
                        "INSERT INTO duplicate_group_members (group_id, record_id, is_representative) VALUES (?, ?, 0)",
                        (group_id, rid)
                    )
                    
    insert_groups(by_pmid, "exact_pmid")
    insert_groups(by_doi, "exact_doi")
    insert_groups(by_pmcid, "exact_pmcid")
    insert_groups(by_title_year, "exact_title_year")
    
    conn.commit()

def run_fuzzy_matcher(conn):
    """Finds fuzzy title duplicates."""
    _assert_qa_gate_passed(conn)
    cursor = conn.cursor()

    # Similar clear step
    cursor.execute("DELETE FROM duplicate_group_members WHERE group_id IN (SELECT group_id FROM duplicate_groups WHERE status = 'pending' AND match_type = 'fuzzy_title')")
    cursor.execute("DELETE FROM duplicate_groups WHERE status = 'pending' AND match_type = 'fuzzy_title'")
    
    # Get remaining unlinked
    cursor.execute("""
        SELECT record_id, title, year 
        FROM records 
        WHERE record_id NOT IN (SELECT record_id FROM study_links)
          AND record_id NOT IN (SELECT record_id FROM duplicate_group_members)
    """)
    records = cursor.fetchall()
    
    # O(N^2) comparison for demonstration (fine for small sets)
    matched = set()
    for i, r1 in enumerate(records):
        if r1["record_id"] in matched: continue
        t1 = normalize_title(r1["title"])
        if not t1: continue
        
        group_members = [r1["record_id"]]
        for j in range(i+1, len(records)):
            r2 = records[j]
            if r2["record_id"] in matched: continue
            if r1["year"] != r2["year"]: continue # Require same year for safety
            
            t2 = normalize_title(r2["title"])
            if not t2: continue
            
            score = difflib.SequenceMatcher(None, t1, t2).ratio()
            if score >= 0.90:
                group_members.append(r2["record_id"])
                
        if len(group_members) > 1:
            group_id = str(uuid4())
            cursor.execute(
                "INSERT INTO duplicate_groups (group_id, match_type, match_key, status) VALUES (?, 'fuzzy_title', ?, 'pending')",
                (group_id, t1[:50])
            )
            for rid in group_members:
                cursor.execute("INSERT INTO duplicate_group_members (group_id, record_id, is_representative) VALUES (?, ?, 0)", (group_id, rid))
                matched.add(rid)
                
    conn.commit()
