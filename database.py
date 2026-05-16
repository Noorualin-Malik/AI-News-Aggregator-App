import sqlite3

DB_NAME = "data/leads.db"

def create_table():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS leads (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        source TEXT,
        url TEXT
    )
    """)

    conn.commit()
    conn.close()

def save_lead(article):

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM leads WHERE url=?
    """, (article["url"],))

    existing = cursor.fetchone()

    if existing:
        conn.close()
        return

    cursor.execute("""
    INSERT INTO leads (title, description, source, url)
    VALUES (?, ?, ?, ?)
    """, (
        article["title"],
        article["description"],
        article["source"],
        article["url"]
    ))

    conn.commit()
    conn.close()
    
    
def get_all_leads():

    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM leads")

    rows = cursor.fetchall()

    conn.close()

    return rows