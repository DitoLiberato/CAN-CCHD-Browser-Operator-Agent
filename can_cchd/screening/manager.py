import datetime
from uuid import uuid4

def get_next_candidate(conn):
    """Fetches the next study to screen, ordered by an implicit or explicit priority."""
    cursor = conn.cursor()
    # In a real scenario, we'd sort by a priority column. 
    # For now, just grab the first 'candidate' study.
    cursor.execute("""
        SELECT study_id, title, first_author, year, journal, pmid, doi 
        FROM studies 
        WHERE status = 'candidate' 
        ORDER BY created_at ASC 
        LIMIT 1
    """)
    row = cursor.fetchone()
    
    if not row:
        return None
        
    study = dict(row)
    # Fetch the abstract. In our simplified DB, abstract is mostly in 'records'.
    # We should grab the abstract from the representative record if study abstract is empty.
    if not study.get("abstract"):
        cursor.execute("SELECT abstract FROM records r JOIN study_links l ON r.record_id = l.record_id WHERE l.study_id = ? AND abstract IS NOT NULL LIMIT 1", (study["study_id"],))
        rec = cursor.fetchone()
        study["abstract"] = rec["abstract"] if rec else "No abstract available."
        
    return study

def save_decision(conn, study_id, decision, reason=None, user="human_physician"):
    """Saves the screening decision and updates the study status."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    # 1. Record decision in audit table
    decision_id = str(uuid4())
    cursor.execute(
        """INSERT INTO screening_decisions (decision_id, study_id, decision, reason, decided_by, decided_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (decision_id, study_id, decision, reason, user, now)
    )
    
    # 2. Update study status
    new_status = f"screening_{decision}"
    if decision in ["citation_mining_only", "separate_analysis"]:
        new_status = decision  # special statuses
        
    cursor.execute("UPDATE studies SET status = ?, updated_at = ? WHERE study_id = ?", (new_status, now, study_id))
    
    conn.commit()

def get_screening_progress(conn):
    """Returns counts of pending and completed screening items."""
    cursor = conn.cursor()
    cursor.execute("SELECT status, count(*) as c FROM studies GROUP BY status")
    counts = {row["status"]: row["c"] for row in cursor.fetchall()}
    
    pending = counts.get("candidate", 0)
    
    completed_statuses = ["screening_include", "screening_maybe", "screening_exclude", "citation_mining_only", "separate_analysis"]
    completed = sum(counts.get(s, 0) for s in completed_statuses)
    
    total = pending + completed
    return {"pending": pending, "completed": completed, "total": total}
