from pathlib import Path
import sqlite3

DB_PATH = Path(__file__).parent / "hotel.db"

def get_connection():
    pragma = "PRAGMA foreign_keys = ON"
    conn = sqlite3.connect(DB_PATH)
    conn.execute(pragma)
    return conn