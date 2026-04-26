import datetime
import json
from uuid import uuid4

def get_next_candidate(conn):
    """Fetches the next study pending eligibility review."""
    cursor = conn.cursor()
    # We only review studies that passed Phase 3 (Include/Maybe)
    # AND passed Phase 4 (meaning they have a fulltext_record)
    # AND haven't been reviewed in Phase 5 yet.
    # Phase 5 updates status to included_quantitative, exclude_full_text, etc.
    cursor.execute("""
        SELECT s.study_id, s.title, s.first_author, s.year, s.journal, s.doi, s.pmid, f.file_path, f.note as retrieval_note
        FROM studies s
        JOIN fulltext_records f ON s.study_id = f.study_id
        WHERE s.status IN ('screening_include', 'screening_maybe')
        ORDER BY s.year DESC
        LIMIT 1
    """)
    row = cursor.fetchone()
    return dict(row) if row else None

def save_decision(conn, study_id, decision, checklist, reason=None, user="human_physician"):
    """Saves the eligibility decision and updates the study status."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    # 1. Record decision
    decision_id = str(uuid4())
    cursor.execute(
        """INSERT INTO eligibility_decisions (decision_id, study_id, decision, checklist_json, reason, decided_by, decided_at)
           VALUES (?, ?, ?, ?, ?, ?, ?)""",
        (decision_id, study_id, decision, json.dumps(checklist), reason, user, now)
    )
    
    # 2. Update study status
    cursor.execute("UPDATE studies SET status = ?, updated_at = ? WHERE study_id = ?", (decision, now, study_id))
    
    conn.commit()

def get_eligibility_progress(conn):
    """Returns counts for the eligibility phase progress."""
    cursor = conn.cursor()
    
    # Total candidates are studies that have a fulltext record AND were originally included/maybe
    cursor.execute("""
        SELECT count(*) as c 
        FROM studies s
        JOIN fulltext_records f ON s.study_id = f.study_id
        WHERE s.status IN ('screening_include', 'screening_maybe', 'included_quantitative', 'exclude_full_text', 'citation_mining_only', 'separate_analysis', 'not_retrieved')
        -- the list of statuses here includes the target states of Phase 5 so we can count total accurately
        -- wait, a better way: any study that has a screening_decision of include/maybe and has a fulltext record
    """)
    # Actually, simpler:
    cursor.execute("""
        SELECT s.status, count(*) as c FROM studies s
        JOIN fulltext_records f ON s.study_id = f.study_id
        GROUP BY s.status
    """)
    counts = {row["status"]: row["c"] for row in cursor.fetchall()}
    
    pending = counts.get("screening_include", 0) + counts.get("screening_maybe", 0)
    
    completed_statuses = ["included_quantitative", "exclude_full_text", "citation_mining_only", "separate_analysis", "not_retrieved"]
    completed = sum(counts.get(s, 0) for s in completed_statuses)
    
    total = pending + completed
    return {"pending": pending, "completed": completed, "total": total}
