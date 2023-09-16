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
    with SQLiteConnectionManager('./sample.db') as c:
        print ("inside With Block")
        c.execute("CREATE TABLE CMDB (id text, server_ip text, base_image text)")
        c.execute("INSERT INTO CMDB VALUES ('i-12345', '10.1.1.1', 'RHEL8')")
        c.execute("INSERT INTO CMDB VALUES ('i-12346', '10.1.1.2', 'RHEL7')")
        c.execute("SELECT * FROM CMDB")
        result = c.fetchall()
        print(result)
    print ("After With Block")