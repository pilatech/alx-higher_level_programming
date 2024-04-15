#!/usr/bin/python3
"""List states that start with N from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    hst = "localhost"

    conn = MySQLdb.connect(host=hst, port=3306, user=usr, passwd=pw, db=db)
    cur = conn.cursor()

    sql = """SELECT * FROM states WHERE name LIKE %s  ORDER BY id"""
    cur.execute(sql, ("N%", ))
    states = cur.fetchall()
    for state in states:
        print(state)
