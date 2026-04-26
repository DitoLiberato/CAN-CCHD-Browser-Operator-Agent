import datetime
import os

def get_retrieval_queue(conn):
    """Fetches all studies that need full-text retrieval."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.study_id, s.title, s.first_author, s.year, s.journal, s.doi, s.pmid, s.status as screening_status
        FROM studies s
        LEFT JOIN fulltext_records f ON s.study_id = f.study_id
        WHERE s.status IN ('screening_include', 'screening_maybe', 'separate_analysis')
          AND f.study_id IS NULL
        ORDER BY s.year DESC
    """)
    return cursor.fetchall()

def save_retrieval_status(conn, study_id, status, file_path=None, note=None):
    """Saves the retrieval outcome for a study."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute(
        """INSERT OR REPLACE INTO fulltext_records (study_id, status, file_path, note, retrieved_at)
           VALUES (?, ?, ?, ?, ?)""",
        (study_id, status, file_path, note, now)
    )
    conn.commit()

def get_retrieval_progress(conn):
    """Returns counts for the retrieval phase progress."""
    cursor = conn.cursor()
    
    # Total eligible studies
    cursor.execute("SELECT count(*) as c FROM studies WHERE status IN ('screening_include', 'screening_maybe', 'separate_analysis')")
    total = cursor.fetchone()["c"]
    
    # Completed retrievals (either downloaded, manual, or unobtainable)
    cursor.execute("""
        SELECT count(*) as c FROM fulltext_records f
        JOIN studies s ON f.study_id = s.study_id
        WHERE s.status IN ('screening_include', 'screening_maybe', 'separate_analysis')
    """)
    completed = cursor.fetchone()["c"]
    
    pending = total - completed
    return {"pending": pending, "completed": completed, "total": total}
