import datetime
from uuid import uuid4

def run_all_checks(conn):
    """Executes all QA rules and records findings."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    # 1. Clear previous open findings (we do a fresh scan every time)
    cursor.execute("DELETE FROM qa_findings WHERE status = 'open'")
    
    # We will only look at studies that reached at least Phase 5 (included_quantitative)
    cursor.execute("SELECT study_id, title FROM studies WHERE status IN ('included_quantitative', 'mapping_completed')")
    active_studies = cursor.fetchall()
    
    for study in active_studies:
        sid = study["study_id"]
        
        # Check 1: Missing Primary Denominator (number_cchd_negative_failed)
        cursor.execute("SELECT status, value_numeric FROM extraction_fields WHERE study_id = ? AND field_name = 'number_cchd_negative_failed'", (sid,))
        denom = cursor.fetchone()
        
        if not denom or denom["status"] not in ["verified", "corrected"] or denom["value_numeric"] is None:
            _add_finding(cursor, "Missing Denominator", "critical", "Primary denominator 'number_cchd_negative_failed' is missing or unverified.", sid, now)
            
        # Check 2: Unverified Fields (AI suggested data would enter analysis)
        cursor.execute("SELECT count(*) as c FROM extraction_fields WHERE study_id = ? AND status IN ('ai_suggested', 'human_extracted')", (sid,))
        if cursor.fetchone()["c"] > 0:
            _add_finding(cursor, "Unverified Fields", "critical", "Study has fields that have not been verified.", sid, now)
            
        # Check 3: Consistency - CAN-CCHD > Denominator
        cursor.execute("SELECT value_numeric FROM extraction_fields WHERE study_id = ? AND field_name = 'number_can_cchd' AND status IN ('verified', 'corrected')", (sid,))
        can_cchd = cursor.fetchone()
        
        if denom and can_cchd and denom["value_numeric"] is not None and can_cchd["value_numeric"] is not None:
            if can_cchd["value_numeric"] > denom["value_numeric"]:
                _add_finding(cursor, "Logical Consistency", "critical", f"Number of CAN-CCHD cases ({can_cchd['value_numeric']}) is greater than the denominator ({denom['value_numeric']}).", sid, now)
                
    conn.commit()

def _add_finding(cursor, rule_name, severity, description, study_id, now):
    """Internal helper to insert a finding only if it wasn't already accepted."""
    # Check if this exact rule for this study was already accepted
    cursor.execute("SELECT finding_id FROM qa_findings WHERE study_id = ? AND rule_name = ? AND status = 'accepted_with_note'", (study_id, rule_name))
    if not cursor.fetchone():
        cursor.execute(
            """INSERT INTO qa_findings (finding_id, rule_name, severity, description, study_id, status, created_at, updated_at)
               VALUES (?, ?, ?, ?, ?, 'open', ?, ?)""",
            (str(uuid4()), rule_name, severity, description, study_id, now, now)
        )

def get_open_findings(conn):
    """Returns all blocking QA findings."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT f.*, s.title 
        FROM qa_findings f
        LEFT JOIN studies s ON f.study_id = s.study_id
        WHERE f.status = 'open'
        ORDER BY f.severity ASC, s.title ASC
    """)
    return [dict(r) for r in cursor.fetchall()]

def override_finding(conn, finding_id, note):
    """Overrides a finding by accepting it with a mandatory note."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    cursor.execute("UPDATE qa_findings SET status = 'accepted_with_note', resolution_note = ?, updated_at = ? WHERE finding_id = ?", (note, now, finding_id))
    conn.commit()
