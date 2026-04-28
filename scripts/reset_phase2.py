import sqlite3
from pathlib import Path

db_path = "data/processed/can_cchd_agent.db"
conn = sqlite3.connect(db_path)
c = conn.cursor()

print("Cleaning up Phase 2...")
c.execute("DELETE FROM study_links")
c.execute("DELETE FROM studies")
c.execute("DELETE FROM duplicate_group_members")
c.execute("DELETE FROM duplicate_groups")
c.execute("UPDATE workflow_phases SET status = 'available' WHERE phase_id = '2'")

conn.commit()
conn.close()
print("Reset complete. Phase 2 is now fresh.")
