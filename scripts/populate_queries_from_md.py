import sys
import os
import re
from uuid import uuid4

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from can_cchd.db.connection import get_connection

def populate_from_md():
    md_path = "CAN-CCHD_Database_Search_Instructions_All_Platforms.md"
    if not os.path.exists(md_path):
        print(f"Error: {md_path} not found.")
        return

    with open(md_path, "r", encoding="utf-8") as f:
        content = f.read()

    conn = get_connection()
    cursor = conn.cursor()

    # Get active protocol version
    cursor.execute("SELECT protocol_version_id FROM protocol_versions ORDER BY version_number DESC LIMIT 1")
    row = cursor.fetchone()
    if not row:
        print("Error: No protocol version found. Initialize Phase 0 first.")
        return
    proto_id = row["protocol_version_id"]

    # Clear existing sources and queries for this protocol to avoid mess
    cursor.execute("DELETE FROM research_queries WHERE source_id IN (SELECT source_id FROM research_sources WHERE protocol_version_id = ?)", (proto_id,))
    cursor.execute("DELETE FROM research_sources WHERE protocol_version_id = ?", (proto_id,))

    # Regex patterns
    source_pattern = re.compile(r'^# (\d+)\. (.+)$', re.MULTILINE)
    query_pattern = re.compile(r'^## (.+) — (.+)\n\n```text\n([\s\S]+?)\n```', re.MULTILINE)

    # 1. Extract Sources
    sources_found = source_pattern.findall(content)
    source_map = {} # name -> id

    for order, name in sources_found:
        source_id = str(uuid4())
        source_map[name.strip()] = source_id
        
        # Determine access mode from the markdown if possible, or default
        access_mode = "API-autonomous"
        if "Embase" in name or "Scopus" in name or "Web of Science" in name:
            access_mode = "Supervised-login"
        elif "Google Scholar" in name:
            access_mode = "Browser-supervised"

        cursor.execute(
            """INSERT INTO research_sources (source_id, protocol_version_id, source_name, priority_order, access_mode, status, records_found, records_imported)
               VALUES (?, ?, ?, ?, ?, 'pending', 0, 0)""",
            (source_id, proto_id, name.strip(), int(order), access_mode)
        )
        print(f"Added Source: {name.strip()}")

    # 2. Extract Queries
    queries_found = query_pattern.findall(content)
    for source_name_full, label, q_string in queries_found:
        # Match source_name_full back to our source_map
        # E.g., "PubMed" should match "PubMed / MEDLINE"
        matched_source_id = None
        for s_name, s_id in source_map.items():
            if s_name.split(' ')[0] in source_name_full:
                matched_source_id = s_id
                break
        
        if matched_source_id:
            cursor.execute(
                """INSERT INTO research_queries (query_id, source_id, query_label, query_string, status, result_count, records_imported)
                   VALUES (?, ?, ?, ?, 'pending', 0, 0)""",
                (str(uuid4()), matched_source_id, label.strip(), q_string.strip())
            )
            print(f"  Added Query for {source_name_full}: {label.strip()}")

    conn.commit()
    conn.close()
    print("Done populating database from markdown.")

if __name__ == "__main__":
    populate_from_md()
