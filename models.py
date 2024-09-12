import sqlite3

class Todo:
    id = None
    name = None
    complete = False

    def __init__(self, id=None,name=None,complete=False) -> None:
        self.id = id
        self.name = name
        self.complete = complete

    @staticmethod
    def list(*args, db: sqlite3.Connection):
        results = []
        rows = db.execute('SELECT id, name, complete FROM todos')
        for row in rows:
            results.append(Todo(id=row[0], name=row[1], complete=row[2]))
        return results

    @staticmethod
    def create(*args, db: sqlite3.Connection):
        db.execute('INSERT INTO todos (name) VALUES (?)', args[0])
        db.commit()
        rows = db.execute('SELECT id, name, complete FROM todos WHERE name=? ORDER BY id DESC', args[0])
        row = rows.fetchone()
        return Todo(id=row[0], name=row[1], complete=row[2])

    @staticmethod
    def find(*args, db: sqlite3.Connection):
        rows = db.execute('SELECT id, name, complete FROM todos WHERE id=?', args[0])
        row = rows.fetchone()
        return Todo(id=row[0], name=row[1], complete=row[2])

    @staticmethod
    def delete(*args, db: sqlite3.Connection):
        todo = Todo.find(args[0], db=db)
        db.execute('DELETE FROM todos WHERE id=?', args[0])
        db.commit()
        return todo

    @staticmethod
    def complete(*args, db: sqlite3.Connection):
        db.execute('UPDATE todos SET complete=? WHERE id=?', [True, args[0][0]])
        db.commit()
        return Todo.find(args[0], db=db)