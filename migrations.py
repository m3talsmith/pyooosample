import sqlite3

def migrate():
    db = sqlite3.connect('todo.sqlite')

    db.execute("""
CREATE TABLE IF NOT EXISTS todos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name varchar(255),
    complete bool
)
    """)