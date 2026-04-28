import datetime
from uuid import uuid4

def evaluate_priority(title, abstract):
    text = f"{title or ''} {abstract or ''}".lower()
    
    high_terms = ['cchd', 'critical congenital heart disease', 'pulse oximetry', 'oxygen saturation', 'false positive', 'failed screen', 'pphn']
    neg_terms = ['adult', 'prenatal only', 'animal', 'surgery only']
    
    for term in neg_terms:
        if term in text: return "very_low"
        
    score = sum(1 for term in high_terms if term in text)
    if score >= 2: return "high"
    if score == 1: return "medium"
    return "low"

def bulk_merge_exact(conn):
    """Merges all pending exact duplicate groups."""
    cursor = conn.cursor()
    cursor.execute("SELECT group_id, match_type FROM duplicate_groups WHERE status = 'pending' AND match_type LIKE 'exact_%'")
    groups = cursor.fetchall()
    
    now = datetime.datetime.now(datetime.UTC).isoformat()
    merged_count = 0
    
    for group in groups:
        gid = group["group_id"]
        cursor.execute("SELECT r.* FROM records r JOIN duplicate_group_members m ON r.record_id = m.record_id WHERE m.group_id = ?", (gid,))
        members = cursor.fetchall()
        
        if not members: continue
        
        # Determine representative (simplified: pick first with PMID, then DOI, else first)
        rep = members[0]
        for m in members:
            if m["pmid"]: rep = m; break
            if m["doi"]: rep = m
            
        study_id = str(uuid4())
        priority = evaluate_priority(rep["title"], rep["abstract"])
        
        # Create study
        cursor.execute(
            """INSERT INTO studies (study_id, title, first_author, year, journal, doi, pmid, pmcid, status, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (study_id, rep["title"], rep["authors"], rep["year"], rep["journal"], rep["doi"], rep["pmid"], rep["pmcid"], "candidate", now)
        )
        
        # Link records
        for m in members:
            cursor.execute("INSERT INTO study_links (study_id, record_id) VALUES (?, ?)", (study_id, m["record_id"]))
            
        # Update group status
        cursor.execute("UPDATE duplicate_groups SET status = 'merged' WHERE group_id = ?", (gid,))
        merged_count += 1
        
    conn.commit()
    return merged_count

def process_singletons(conn):
    """Converts unlinked records into single studies if no groups remain."""
    cursor = conn.cursor()
    cursor.execute("""
        SELECT * FROM records 
        WHERE record_id NOT IN (SELECT record_id FROM study_links)
          AND record_id NOT IN (SELECT record_id FROM duplicate_group_members m JOIN duplicate_groups g ON m.group_id = g.group_id WHERE g.status = 'pending')
    """)
    singletons = cursor.fetchall()
    
    now = datetime.datetime.now(datetime.UTC).isoformat()
    for rec in singletons:
        study_id = str(uuid4())
        cursor.execute(
            """INSERT INTO studies (study_id, title, first_author, year, journal, doi, pmid, pmcid, status, created_at)
               VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (study_id, rec["title"], rec["authors"], rec["year"], rec["journal"], rec["doi"], rec["pmid"], rec["pmcid"], "candidate", now)
        )
        cursor.execute("INSERT INTO study_links (study_id, record_id) VALUES (?, ?)", (study_id, rec["record_id"]))
        
    conn.commit()

def merge_group_manual(conn, group_id, notes=None):
    """Merges a specific group manually."""
    cursor = conn.cursor()
    cursor.execute("SELECT r.* FROM records r JOIN duplicate_group_members m ON r.record_id = m.record_id WHERE m.group_id = ?", (group_id,))
    members = cursor.fetchall()
    
    if not members: return False
    
    # Representative logic
    rep = members[0]
    for m in members:
        if m["pmid"]: rep = m; break
        if m["doi"]: rep = m
        
    study_id = str(uuid4())
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    cursor.execute(
        """INSERT INTO studies (study_id, title, first_author, year, journal, doi, pmid, pmcid, status, created_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (study_id, rep["title"], rep["authors"], rep["year"], rep["journal"], rep["doi"], rep["pmid"], rep["pmcid"], "candidate", now)
    )
    
    for m in members:
        cursor.execute("INSERT INTO study_links (study_id, record_id) VALUES (?, ?)", (study_id, m["record_id"]))
        
    cursor.execute("UPDATE duplicate_groups SET status = 'merged' WHERE group_id = ?", (group_id,))
    conn.commit()
    return True

def reject_group_manual(conn, group_id):
    """Marks a group as rejected (records are not duplicates)."""
    cursor = conn.cursor()
    cursor.execute("UPDATE duplicate_groups SET status = 'rejected' WHERE group_id = ?", (group_id,))
    conn.commit()
    return True
