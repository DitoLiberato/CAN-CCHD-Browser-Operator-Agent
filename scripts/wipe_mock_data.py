import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from can_cchd.db.connection import get_connection

def wipe_mock_data():
    conn = get_connection()
    cursor = conn.cursor()
    
    # 1. Delete all mock evidence data
    tables_to_clear = [
        "records",
        "studies",
        "duplicate_groups",
        "fulltext_records",
        "eligibility_decisions",
        "extraction_tasks",
        "extraction_fields",
        "diagnosis_mappings",
        "qa_findings",
        "agent_action_log"
    ]
    
    for table in tables_to_clear:
        try:
            cursor.execute(f"DELETE FROM {table}")
        except Exception as e:
            print(f"Skipping {table}: {e}")
            
    # 2. Reset research sources
    cursor.execute("""
        UPDATE research_sources 
        SET status = 'pending', records_found = 0, records_imported = 0, 
            records_unique_after_dedup = 0, completed_at = NULL
    """)
    
    # 3. Reset workflow phases (Keep Phase 0 complete, Phase 1 in progress)
    cursor.execute("UPDATE workflow_phases SET status = 'pending'")
    cursor.execute("UPDATE workflow_phases SET status = 'completed' WHERE phase_id = '0'")
    cursor.execute("UPDATE workflow_phases SET status = 'in_progress' WHERE phase_id = '1'")
    
    conn.commit()
    print("Mock data wiped successfully. The system is ready for real data!")

if __name__ == "__main__":
    wipe_mock_data()
