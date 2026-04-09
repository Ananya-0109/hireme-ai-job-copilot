import sqlite3

conn = sqlite3.connect("jobs.db", check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS applications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    job_title TEXT,
    company TEXT,
    status TEXT
)
""")
conn.commit()

def save_application(job_title, company, status="Applied"):
    cursor.execute(
        "INSERT INTO applications (job_title, company, status) VALUES (?, ?, ?)",
        (job_title, company, status)
    )
    conn.commit()

def get_applications():
    cursor.execute("SELECT * FROM applications")
    return cursor.fetchall()