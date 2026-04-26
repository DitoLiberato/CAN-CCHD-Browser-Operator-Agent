import sys
import os
import datetime
from uuid import uuid4

# Ensure module can be found
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from can_cchd.db.connection import get_connection

def seed_database():
    conn = get_connection()
    cursor = conn.cursor()
    
    # Check if records already exist
    cursor.execute("SELECT count(*) as c FROM records")
    if cursor.fetchone()["c"] > 0:
        print("Database already has records, skipping seed.")
        return
        
    now = datetime.datetime.now(datetime.UTC).isoformat()
    
    records = [
        # Exact PMID match (Group 1)
        {
            "record_id": str(uuid4()), "source_id": "mock_1", "query_id": "q1", "source_database": "PubMed", 
            "source_record_id": "PM1", "title": "False positive pulse oximetry screening for critical congenital heart disease",
            "authors": "Smith J, Doe A", "year": 2023, "journal": "Pediatrics", "doi": "10.1542/peds.2023-1",
            "pmid": "30000001", "pmcid": "", "abstract": "Pulse oximetry screening resulted in 15 false positives. 3 had PPHN.",
            "url": "", "pdf_url": "", "is_open_access": 1, "metadata_json": "{}", "imported_at": now
        },
        {
            "record_id": str(uuid4()), "source_id": "mock_2", "query_id": "q2", "source_database": "Embase", 
            "source_record_id": "EM1", "title": "False-positive pulse oximetry screening for critical congenital heart disease",
            "authors": "Smith J", "year": 2023, "journal": "Pediatrics", "doi": "10.1542/peds.2023-1",
            "pmid": "30000001", "pmcid": "", "abstract": "Short abstract here.",
            "url": "", "pdf_url": "", "is_open_access": 0, "metadata_json": "{}", "imported_at": now
        },
        
        # Exact DOI match (Group 2)
        {
            "record_id": str(uuid4()), "source_id": "mock_1", "query_id": "q1", "source_database": "PubMed", 
            "source_record_id": "PM2", "title": "Incidence of secondary conditions after failed CCHD screen",
            "authors": "Jones B", "year": 2022, "journal": "J Pediatr", "doi": "10.1016/j.jpeds.2022.01.001",
            "pmid": "30000002", "pmcid": "", "abstract": "We found sepsis in 10% of failed screens.",
            "url": "", "pdf_url": "", "is_open_access": 0, "metadata_json": "{}", "imported_at": now
        },
        {
            "record_id": str(uuid4()), "source_id": "mock_3", "query_id": "q3", "source_database": "Scopus", 
            "source_record_id": "SC1", "title": "Incidence of secondary conditions after failed CCHD screen",
            "authors": "Jones B, et al", "year": 2022, "journal": "Journal of Pediatrics", "doi": "10.1016/j.jpeds.2022.01.001",
            "pmid": "", "pmcid": "", "abstract": "",
            "url": "", "pdf_url": "", "is_open_access": 0, "metadata_json": "{}", "imported_at": now
        },
        
        # Fuzzy match (Group 3)
        {
            "record_id": str(uuid4()), "source_id": "mock_1", "query_id": "q1", "source_database": "PubMed", 
            "source_record_id": "PM3", "title": "Clinical outcomes of neonates with abnormal oxygen saturation but normal echocardiogram",
            "authors": "Lee C", "year": 2021, "journal": "Arch Dis Child", "doi": "10.1136/adc.2021.1",
            "pmid": "30000003", "pmcid": "", "abstract": "Most had respiratory distress.",
            "url": "", "pdf_url": "", "is_open_access": 1, "metadata_json": "{}", "imported_at": now
        },
        {
            "record_id": str(uuid4()), "source_id": "mock_2", "query_id": "q4", "source_database": "Embase", 
            "source_record_id": "EM2", "title": "Clinical outcomes of neonates with abnormal oxygen saturation and normal echocardiography",
            "authors": "Lee C, Kim Y", "year": 2021, "journal": "Arch Dis Child Fetal Neonatal Ed", "doi": "10.1136/adc.2021.1-alt",
            "pmid": "", "pmcid": "", "abstract": "Respiratory distress was common.",
            "url": "", "pdf_url": "", "is_open_access": 0, "metadata_json": "{}", "imported_at": now
        },
        
        # Singleton (No match)
        {
            "record_id": str(uuid4()), "source_id": "mock_1", "query_id": "q1", "source_database": "PubMed", 
            "source_record_id": "PM4", "title": "Cost effectiveness of CCHD screening in rural areas",
            "authors": "Wang D", "year": 2020, "journal": "Health Econ", "doi": "10.1002/hec.2020.1",
            "pmid": "30000004", "pmcid": "", "abstract": "Very cost effective.",
            "url": "", "pdf_url": "", "is_open_access": 1, "metadata_json": "{}", "imported_at": now
        }
    ]
    
    for r in records:
        cursor.execute(
            """INSERT INTO records (
                record_id, source_id, query_id, source_database, source_record_id, title, authors, year, 
                journal, doi, pmid, pmcid, abstract, url, pdf_url, is_open_access, metadata_json, imported_at
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
            (r["record_id"], r["source_id"], r["query_id"], r["source_database"], r["source_record_id"], 
             r["title"], r["authors"], r["year"], r["journal"], r["doi"], r["pmid"], r["pmcid"], 
             r["abstract"], r["url"], r["pdf_url"], r["is_open_access"], r["metadata_json"], r["imported_at"])
        )
        
    conn.commit()
    print("Test records seeded successfully.")

if __name__ == "__main__":
    seed_database()
