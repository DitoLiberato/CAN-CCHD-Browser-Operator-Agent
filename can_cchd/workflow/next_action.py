def get_next_action(conn):
    """
    Evaluates the workflow_phases table and determines the next available action.
    Returns a dict with: phase, priority, message, target_component, blocking.
    """
    cursor = conn.cursor()
    
    # Define phase sequence (0-11)
    phase_order = [
        ("0", "Research Plan"),
        ("1", "Search Collection"),
        ("2", "Deduplication"),
        ("3", "Title/Abstract Screening"),
        ("4", "Full-Text Retrieval"),
        ("5", "Full-Text Eligibility"),
        ("6", "Data Extraction"),
        ("7", "Extraction Verification"),
        ("8", "Diagnosis Mapping"),
        ("9", "QA Sentinel"),
        ("10", "Analysis"),
        ("11", "Manuscript / Abstract Draft")
    ]
    
    # Get current phase states
    import sqlite3
    try:
        cursor.execute("SELECT phase_id, phase_order, status FROM workflow_phases ORDER BY phase_order ASC")
        phases = {row["phase_id"]: row for row in cursor.fetchall()}
    except sqlite3.OperationalError:
        phases = {}
    
    # If table is empty, initialize it
    if not phases:
        for p_id, p_name in phase_order:
            status = "available" if p_id == "0" else "locked"
            cursor.execute(
                """INSERT INTO workflow_phases (phase_id, phase_order, phase_name, status) 
                   VALUES (?, ?, ?, ?)""",
                (p_id, int(p_id), p_name, status)
            )
        conn.commit()
        
        cursor.execute("SELECT phase_id, phase_order, status FROM workflow_phases ORDER BY phase_order ASC")
        phases = {row["phase_id"]: row for row in cursor.fetchall()}
        
    for p_id, p_name in phase_order:
        phase = phases.get(p_id)
        if not phase:
            continue
            
        status = phase["status"]
        if status in ["locked", "available", "in_progress", "blocked"]:
            # This is the active phase we need to address
            return {
                "phase_id": p_id,
                "phase_name": p_name,
                "status": status,
                "message": f"Phase {p_id} ({p_name}) is currently {status}.",
                "blocking": status in ["locked", "blocked"]
            }
            
    return {
        "phase_id": "12",
        "phase_name": "Completed",
        "status": "completed",
        "message": "All phases are completed.",
        "blocking": False
    }

def update_phase_status(conn, phase_id, status, note=None):
    """Updates the status of a specific phase and potentially unlocks the next phase."""
    cursor = conn.cursor()
    
    cursor.execute(
        "UPDATE workflow_phases SET status = ?, completion_note = ? WHERE phase_id = ?",
        (status, note, phase_id)
    )
    
    # Simple gating rule: if this phase is completed, unlock the next one
    if status in ["completed", "completed_with_note", "skipped_with_justification"]:
        next_phase_id = str(int(phase_id) + 1)
        cursor.execute(
            "UPDATE workflow_phases SET status = 'available' WHERE phase_id = ? AND status = 'locked'",
            (next_phase_id,)
        )
        
    conn.commit()
