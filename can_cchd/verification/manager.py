import datetime
from uuid import uuid4
from can_cchd.extraction.manager import save_field

def get_verification_queue(conn):
    """Fetches studies that are fully extracted and ready for verification."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.study_id, s.title, s.first_author, s.year, s.journal
        FROM studies s
        JOIN extraction_tasks t ON s.study_id = t.study_id
        WHERE t.status = 'completed'
        ORDER BY s.year DESC
    """)
    return cursor.fetchall()

def get_fields_for_verification(conn, study_id):
    """Fetches all fields extracted in Phase 6."""
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM extraction_fields WHERE study_id = ?", (study_id,))
    return [dict(r) for r in cursor.fetchall()]

def verify_field(conn, field_id, new_status, corrected_value_raw=None, corrected_value_numeric=None):
    """Updates the verification status of a specific field."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    if corrected_value_raw is not None:
        cursor.execute(
            "UPDATE extraction_fields SET status = ?, value_raw = ?, value_numeric = ?, updated_at = ? WHERE field_id = ?",
            (new_status, corrected_value_raw, corrected_value_numeric, now, field_id)
        )
    else:
        cursor.execute(
            "UPDATE extraction_fields SET status = ?, updated_at = ? WHERE field_id = ?",
            (new_status, now, field_id)
        )
    conn.commit()

def calculate_denominator_suggestion(conn, study_id):
    """Checks if calculation for number_cchd_negative_failed is possible and suggests it."""
    cursor = conn.cursor()
    
    cursor.execute("SELECT status, value_numeric FROM extraction_fields WHERE study_id = ? AND field_name = 'number_failed_screen'", (study_id,))
    failed = cursor.fetchone()
    
    cursor.execute("SELECT status, value_numeric FROM extraction_fields WHERE study_id = ? AND field_name = 'number_cchd'", (study_id,))
    cchd = cursor.fetchone()
    
    if failed and cchd:
        # Both must be verified or corrected
        if failed["status"] in ["verified", "corrected"] and cchd["status"] in ["verified", "corrected"]:
            if failed["value_numeric"] is not None and cchd["value_numeric"] is not None:
                calc_val = failed["value_numeric"] - cchd["value_numeric"]
                return calc_val
                
    return None

def apply_calculated_denominator(conn, study_id, calc_val):
    """Saves the calculated denominator as a verified field."""
    save_field(conn, study_id, "number_cchd_negative_failed", str(calc_val), calc_val, source_location="Calculated (Verified)", supporting_quote=f"Calculated from Verified Failed - Verified CCHD", status="verified")

def mark_study_verified(conn, study_id):
    """Marks the study as fully verified in the extraction_tasks table."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    cursor.execute("UPDATE extraction_tasks SET status = 'verified', updated_at = ? WHERE study_id = ?", (now, study_id))
    conn.commit()

def get_verification_progress(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) as c FROM extraction_tasks WHERE status IN ('completed', 'verified')")
    total = cursor.fetchone()["c"]
    
    cursor.execute("SELECT count(*) as c FROM extraction_tasks WHERE status = 'verified'")
    completed = cursor.fetchone()["c"]
    
    return {"pending": total - completed, "completed": completed, "total": total}
