import datetime
from uuid import uuid4

def get_next_candidate(conn):
    """Fetches the next study to screen, ordered by an implicit or explicit priority."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT study_id, title, first_author, year, journal, pmid, doi, abstract,
               linked_record_count, source_databases_json, query_labels_json
        FROM unique_studies
        WHERE screening_status = 'not_started'
        ORDER BY created_at ASC 
        LIMIT 1
    """)
    row = cursor.fetchone()
    
    if not row:
        return None
        
    study = dict(row)
    study["abstract"] = study.get("abstract") or "No abstract available."
    return study

def save_decision(conn, study_id, decision, reason=None, user="human_physician"):
    """Saves the screening decision and updates the unique study screening status."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    # 1. Record decision in audit table
    decision_id = str(uuid4())
    cursor.execute(
        """INSERT INTO screening_decisions (decision_id, study_id, decision, reason, decided_by, decided_at)
           VALUES (?, ?, ?, ?, ?, ?)""",
        (decision_id, study_id, decision, reason, user, now)
    )
    
    new_status = decision
    if decision in ["citation_mining_only", "separate_analysis"]:
        new_status = decision

    cursor.execute(
        "UPDATE unique_studies SET screening_status = ?, updated_at = ? WHERE study_id = ?",
        (new_status, now, study_id),
    )
    
    conn.commit()

def get_screening_progress(conn):
    """Returns counts of pending and completed screening items."""
    cursor = conn.cursor()
    cursor.execute("SELECT screening_status, count(*) as c FROM unique_studies GROUP BY screening_status")
    counts = {row["screening_status"]: row["c"] for row in cursor.fetchall()}

    pending = counts.get("not_started", 0)

    completed_statuses = ["include", "maybe", "exclude", "citation_mining_only", "separate_analysis"]
    completed = sum(counts.get(s, 0) for s in completed_statuses)

    total = pending + completed
    return {"pending": pending, "completed": completed, "total": total}
