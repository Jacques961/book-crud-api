import sqlite3

# Connect to SQLite and create the database file if not exists
conn = sqlite3.connect('books.db')
cursor = conn.cursor()

# Create the books table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        year INTEGER NOT NULL
    )
''')

# Insert initial books (if table is empty)
cursor.execute("SELECT COUNT(*) FROM books")
if cursor.fetchone()[0] == 0:
    books = [
        ("1984", "George Orwell", 1949),
        ("The Little Prince", "Antoine de Saint-Exupéry", 1943),
        ("Sapiens", "Yuval Noah Harari", 2011),
    ]
    cursor.executemany("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", books)
    conn.commit()

conn.close()
