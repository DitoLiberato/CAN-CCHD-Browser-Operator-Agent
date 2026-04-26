import sqlite3
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Determine DB path from .env or default
DB_PATH = os.getenv("DB_PATH", "data/processed/can_cchd_agent.db")

def get_connection():
    """Returns a connection to the SQLite database. Ensures directories exist."""
    db_file = Path(DB_PATH)
    
    # Create parent directories if they don't exist
    db_file.parent.mkdir(parents=True, exist_ok=True)
    
    conn = sqlite3.connect(str(db_file))
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initializes the database using schema.sql."""
    conn = get_connection()
    schema_path = Path(__file__).parent / "schema.sql"
    
    with open(schema_path, "r", encoding="utf-8") as f:
        schema_sql = f.read()
        
    try:
        conn.executescript(schema_sql)
        conn.commit()
    except Exception as e:
        print(f"Error initializing database: {e}")
        conn.rollback()
    finally:
        conn.close()

if __name__ == "__main__":
    init_db()
    print(f"Database initialized at {DB_PATH}")
