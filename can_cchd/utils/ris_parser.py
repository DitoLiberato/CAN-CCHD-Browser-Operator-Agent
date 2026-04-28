import re
from uuid import uuid4
import datetime

def parse_ris(file_content: str):
    """Parses a generic RIS file and returns a list of dictionaries with extracted fields."""
    records = []
    current_record = {}
    
    for line in file_content.splitlines():
        line = line.strip()
        if not line:
            continue
            
        # Match 'TAG  - Value' or 'TAG - Value'
        match = re.match(r'^([A-Z0-9]{2})\s*-\s*(.*)$', line)
        if match:
            tag, value = match.groups()
            
            if tag == 'TY':
                if current_record:
                    records.append(current_record)
                current_record = {'authors': []}
                
            elif tag == 'TI' or tag == 'T1':
                current_record['title'] = value
                
            elif tag == 'AU' or tag == 'A1':
                current_record['authors'].append(value)
                
            elif tag == 'PY' or tag == 'Y1':
                # Try to extract 4 digit year
                year_match = re.search(r'\d{4}', value)
                if year_match:
                    current_record['year'] = int(year_match.group())
                    
            elif tag == 'DO':
                current_record['doi'] = value
                
            elif tag == 'U1' or tag == 'AN': 
                # Sometimes PMID is stored in custom fields or accession number
                if 'pmid' not in current_record:
                    current_record['pmid'] = value
                    
            elif tag == 'ER':
                if current_record:
                    records.append(current_record)
                current_record = {}
                
    if current_record:
        records.append(current_record)
        
    # Post-process
    final_records = []
    for r in records:
        if 'title' in r:
            final_records.append({
                'title': r.get('title', 'Unknown Title'),
                'authors': ', '.join(r.get('authors', [])),
                'year': r.get('year', 2024),
                'doi': r.get('doi', None),
                'pmid': r.get('pmid', None)
            })
            
    return final_records

def save_manual_records(conn, parsed_records, source_id, query_id, source_name):
    """Saves parsed RIS records into the database using UPSERT logic."""
    cursor = conn.cursor()
    now = datetime.datetime.now(datetime.UTC).isoformat()
    count = 0
    
    for r in parsed_records:
        # Check duplicates in studies
        existing_study = None
        if r['pmid']:
            cursor.execute("SELECT study_id FROM studies WHERE pmid = ?", (r['pmid'],))
            existing_study = cursor.fetchone()
            
        if not existing_study and r['doi']:
            cursor.execute("SELECT study_id FROM studies WHERE doi = ?", (r['doi'],))
            existing_study = cursor.fetchone()
            
        if existing_study:
            study_id = existing_study["study_id"]
        else:
            study_id = str(uuid4())
            cursor.execute(
                """INSERT INTO studies (study_id, title, first_author, year, status, pmid, doi, created_at)
                   VALUES (?, ?, ?, ?, 'initial_collection', ?, ?, ?)""",
                (study_id, r['title'], r['authors'].split(',')[0] if r['authors'] else "", r['year'], r['pmid'], r['doi'], now)
            )
            
        # Insert into records
        cursor.execute("SELECT record_id FROM records WHERE study_id = ? AND query_id = ?", (study_id, query_id))
        if not cursor.fetchone():
            cursor.execute(
                """INSERT INTO records (record_id, study_id, source_id, query_id, source_database, title, authors, year, pmid, doi, imported_at)
                   VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                (str(uuid4()), study_id, source_id, query_id, source_name, r['title'], r['authors'], r['year'], r['pmid'], r['doi'], now)
            )
            count += 1
            
    # Update query stats
    cursor.execute("SELECT records_imported FROM research_queries WHERE query_id = ?", (query_id,))
    row = cursor.fetchone()
    current_query_imported = row["records_imported"] if row else 0
    
    cursor.execute("UPDATE research_queries SET status = 'completed', records_imported = ?, run_at = ? WHERE query_id = ?", 
                   (current_query_imported + count, now, query_id))
                   
    # Update source stats
    cursor.execute("SELECT sum(records_imported) as total FROM research_queries WHERE source_id = ?", (source_id,))
    total_imported = cursor.fetchone()["total"]
    if total_imported is None: total_imported = 0
    
    cursor.execute("UPDATE research_sources SET status = 'completed', records_imported = ? WHERE source_id = ?", (total_imported, source_id))
    
    conn.commit()
    return count
