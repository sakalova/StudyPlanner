import sqlite3


class Database:

    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS study_planner (id INTEGER PRIMARY KEY, data TEXT, status INTEGER)")
        self.conn.commit()

    def insert(self, data, status=0):
        self.cur.execute("INSERT INTO study_planner VALUES (NULL, ?, ?)", (data, status))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT id, data FROM study_planner WHERE status = 0")
        rows = self.cur.fetchall()
        return rows

    def view_p(self):
        self.cur.execute("SELECT id, data FROM study_planner WHERE status = 1")
        rows = self.cur.fetchall()
        return rows

    def view_f(self):
        self.cur.execute("SELECT id, data FROM study_planner WHERE status = 2")
        rows = self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM study_planner WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, data):
        self.cur.execute("UPDATE study_planner SET data=? WHERE id=?", (data, id,))
        self.conn.commit()

    def push_p(self, id):
        self.cur.execute("UPDATE study_planner SET status=1 WHERE id=?", (id,))
        self.conn.commit()

    def push_f(self, id):
        self.cur.execute("UPDATE study_planner SET status=2 WHERE id=?", (id,))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
