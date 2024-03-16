#!/usr/bin/env python

import sqlite3

# context manager
class SQLiteConnectionManager:

    def __init__(self, path):
        self.path = path

    def __enter__(self):
        print ("__enter__")
        self.conn = sqlite3.connect(self.path)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_class, exc, traceback):
        print ("__exit__")
        self.conn.commit()
        self.conn.close()


if __name__ == '__main__':
    print ("Before With Block")
    with SQLiteConnectionMgr('./sample.db') as cur:
        cur.execute("CREATE TABLE movie(title, year, score)")
        cur.execute("""
    INSERT INTO movie VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")

    print ("Data inserted")

    with SQLiteConnectionMgr('./sample.db') as cur:
        res = cur.execute("SELECT * FROM movie")
        print (res.fetchall())


        
    print ("Data fetched")
