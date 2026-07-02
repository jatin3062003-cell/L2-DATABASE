import sqlite3

# Connect to SQLite database
conn = sqlite3.connect("l2_database.db")
cursor = conn.cursor()
def get_connection():
    conn = sqlite3.connect("l2_database.db")
    conn.row_factory = sqlite3.Row
    return conn
print(get_connection())

cursor = conn.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

print(cursor.fetchall())