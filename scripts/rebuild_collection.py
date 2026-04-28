"""
scripts/rebuild_collection.py

Safe reset of the Phase 1 collection pipeline only.
Drops the 5 new collection tables and recreates them from schema.sql.
Does NOT touch studies, records, screening_decisions, or any downstream table.
Resets Phase 1 to 'available' and locks Phase 2.
"""
import sqlite3
import sys
import os
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

DB_PATH = "data/processed/can_cchd_agent.db"
SCHEMA_PATH = "can_cchd/db/schema.sql"

COLLECTION_TABLES = [
    "collection_qa_gate",
    "collection_qa_findings",
    "record_enrichment_log",
    "normalized_records",
    "raw_records",
    "query_runs",
]

def rebuild():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    print("=" * 60)
    print("CAN-CCHD Collection Pipeline Reset")
    print("=" * 60)

    # 1. Drop collection tables in safe order
    print("\n[1/4] Dropping old collection tables...")
    for table in COLLECTION_TABLES:
        c.execute(f"DROP TABLE IF EXISTS {table}")
        print(f"  Dropped: {table}")

    # 2. Recreate from schema.sql
    print("\n[2/4] Recreating tables from schema.sql...")
    with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
        schema = f.read()
    conn.executescript(schema)
    print("  Schema applied successfully.")

    # 3. Reset workflow phases
    print("\n[3/4] Resetting workflow phases...")
    c.execute("UPDATE workflow_phases SET status = 'available' WHERE phase_id = '1'")
    c.execute("UPDATE workflow_phases SET status = 'locked' WHERE phase_id = '2'")
    rows_affected = c.rowcount
    if rows_affected == 0:
        print("  Warning: workflow_phases not found. Inserting Phase 1...")
        c.execute("INSERT OR REPLACE INTO workflow_phases (phase_id, phase_order, phase_name, status) VALUES ('1', 1, 'Search Collection', 'available')")
        c.execute("INSERT OR REPLACE INTO workflow_phases (phase_id, phase_order, phase_name, status) VALUES ('2', 2, 'Deduplication', 'locked')")
    else:
        print("  Phase 1 set to 'available', Phase 2 set to 'locked'.")

    # 4. Initialize QA gate row
    print("\n[4/4] Initializing QA gate...")
    c.execute("""
        INSERT OR REPLACE INTO collection_qa_gate 
        (gate_id, status, total_records, blocking_findings, warning_findings)
        VALUES ('main', 'not_run', 0, 0, 0)
    """)

    conn.commit()
    conn.close()

    print("\n" + "=" * 60)
    print("Reset complete. Phase 1 is ready for fresh collection.")
    print("=" * 60)

if __name__ == "__main__":
    rebuild()
