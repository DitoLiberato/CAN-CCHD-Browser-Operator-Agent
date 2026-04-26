import datetime
from uuid import uuid4

REQUIRED_FIELDS = {
    "characteristics": ["country", "setting", "study_design", "screening_population", "screening_period", "gestational_age", "well_baby_vs_nicu"],
    "denominators": ["number_screened", "number_failed_screen", "number_cchd", "number_cchd_negative_failed"],
    "outcomes": ["number_can_cchd", "number_pphn", "number_respiratory_disease", "number_infection_sepsis", "number_noncritical_chd", "number_no_actionable_diagnosis"]
}

def get_extraction_queue(conn):
    """Fetches studies ready for data extraction."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT study_id, title, first_author, year, journal, pmid, doi
        FROM studies
        WHERE status = 'included_quantitative'
          AND study_id NOT IN (SELECT study_id FROM extraction_tasks WHERE status IN ('completed', 'verified'))
        ORDER BY year DESC
    """)
    return cursor.fetchall()

def get_extracted_fields(conn, study_id):
    """Fetches already extracted fields for a study."""
    cursor = conn.cursor()
    cursor.execute("SELECT field_name, value_raw, value_numeric, source_location, supporting_quote FROM extraction_fields WHERE study_id = ?", (study_id,))
    return {r["field_name"]: dict(r) for r in cursor.fetchall()}

def save_field(conn, study_id, field_name, value_raw, value_numeric=None, source_location=None, supporting_quote=None, status="human_extracted"):
    """Saves a single extracted field."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute("SELECT field_id FROM extraction_fields WHERE study_id = ? AND field_name = ?", (study_id, field_name))
    row = cursor.fetchone()
    
    if row:
        cursor.execute(
            """UPDATE extraction_fields 
               SET value_raw = ?, value_numeric = ?, source_location = ?, supporting_quote = ?, status = ?, updated_at = ?
               WHERE field_id = ?""",
            (value_raw, value_numeric, source_location, supporting_quote, status, now, row["field_id"])
        )
    else:
        cursor.execute(
            """INSERT INTO extraction_fields (field_id, study_id, field_name, value_raw, value_numeric, source_location, supporting_quote, status, updated_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (str(uuid4()), study_id, field_name, value_raw, value_numeric, source_location, supporting_quote, status, now)
        )
    conn.commit()

def mark_study_extracted(conn, study_id):
    """Marks the study as fully extracted and ready for verification."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute("SELECT task_id FROM extraction_tasks WHERE study_id = ?", (study_id,))
    if cursor.fetchone():
        cursor.execute("UPDATE extraction_tasks SET status = 'completed', updated_at = ? WHERE study_id = ?", (now, study_id))
    else:
        cursor.execute("INSERT INTO extraction_tasks (task_id, study_id, status, updated_at) VALUES (?, ?, 'completed', ?)", (str(uuid4()), study_id, now))
        
    conn.commit()

def mock_ai_extract(conn, study_id):
    """Fills the database with fake data for testing."""
    save_field(conn, study_id, "country", "USA", source_location="Page 2", supporting_quote="The study took place in the US.", status="ai_suggested")
    save_field(conn, study_id, "setting", "Multicenter", source_location="Page 2", supporting_quote="Across 5 hospitals.", status="ai_suggested")
    save_field(conn, study_id, "study_design", "Retrospective Cohort", source_location="Abstract", supporting_quote="In this retrospective cohort...", status="ai_suggested")
    save_field(conn, study_id, "number_screened", "100000", 100000, source_location="Results, P3", supporting_quote="We screened 100,000 newborns.", status="ai_suggested")
    save_field(conn, study_id, "number_failed_screen", "100", 100, source_location="Results, P3", supporting_quote="100 failed the initial screen.", status="ai_suggested")
    save_field(conn, study_id, "number_cchd", "20", 20, source_location="Results, P4", supporting_quote="20 were diagnosed with CCHD.", status="ai_suggested")
    save_field(conn, study_id, "number_cchd_negative_failed", "80", 80, source_location="Calculated", supporting_quote="100 failed - 20 CCHD", status="ai_suggested")
    save_field(conn, study_id, "number_can_cchd", "30", 30, source_location="Table 2", supporting_quote="30 had secondary actionable diagnoses.", status="ai_suggested")
    save_field(conn, study_id, "number_pphn", "15", 15, source_location="Table 2", supporting_quote="15 were diagnosed with PPHN.", status="ai_suggested")

def get_extraction_progress(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) as c FROM studies WHERE status = 'included_quantitative'")
    total = cursor.fetchone()["c"]
    
    cursor.execute("SELECT count(*) as c FROM extraction_tasks WHERE status IN ('completed', 'verified')")
    completed = cursor.fetchone()["c"]
    
    return {"pending": total - completed, "completed": completed, "total": total}
