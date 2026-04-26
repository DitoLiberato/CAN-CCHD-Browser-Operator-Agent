import datetime
from uuid import uuid4

CATEGORIES = [
    "pphn",
    "respiratory_disease",
    "infection_sepsis",
    "noncritical_chd",
    "transitional_circulation",
    "no_actionable_diagnosis",
    "other_actionable",
    "unclear"
]

def get_mapping_queue(conn):
    """Fetches studies that are fully verified in Phase 7 and ready for mapping."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.study_id, s.title, s.year, s.status
        FROM studies s
        JOIN extraction_tasks t ON s.study_id = t.study_id
        WHERE t.status = 'verified' AND s.status = 'included_quantitative'
        ORDER BY s.year DESC
    """)
    return cursor.fetchall()

def get_mappings(conn, study_id):
    """Fetches all mappings for a given study."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM diagnosis_mappings WHERE study_id = ? ORDER BY updated_at ASC", (study_id,))
    return [dict(r) for r in cursor.fetchall()]

def add_mapping(conn, study_id, original_term, case_count, source_quote, mapped_category, is_can_cchd, overlap_possible):
    """Adds a new diagnosis mapping."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    cursor.execute(
        """INSERT INTO diagnosis_mappings (mapping_id, study_id, original_term, case_count, source_quote, mapped_category, is_can_cchd, overlap_possible, status, updated_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)""",
        (str(uuid4()), study_id, original_term, case_count, source_quote, mapped_category, int(is_can_cchd), int(overlap_possible), now)
    )
    conn.commit()

def verify_mapping(conn, mapping_id):
    """Marks a mapping as verified."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    cursor.execute("UPDATE diagnosis_mappings SET status = 'verified', updated_at = ? WHERE mapping_id = ?", (now, mapping_id))
    conn.commit()

def delete_mapping(conn, mapping_id):
    """Deletes a mapping."""
    cursor = conn.cursor()
    cursor.execute("DELETE FROM diagnosis_mappings WHERE mapping_id = ?", (mapping_id,))
    conn.commit()

def mark_study_mapped(conn, study_id):
    """Marks the study as fully mapped (Phase 8 completed)."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    # Update study status to indicate mapping is complete
    cursor.execute("UPDATE studies SET status = 'mapping_completed', updated_at = ? WHERE study_id = ?", (now, study_id))
    conn.commit()

def get_mapping_progress(conn):
    cursor = conn.cursor()
    cursor.execute("""
        SELECT count(*) as c FROM extraction_tasks WHERE status = 'verified'
    """)
    total = cursor.fetchone()["c"]
    
    cursor.execute("SELECT count(*) as c FROM studies WHERE status = 'mapping_completed'")
    completed = cursor.fetchone()["c"]
    
    return {"pending": total - completed, "completed": completed, "total": total}
