#!/usr/bin/python3
"""List states that start with N from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    search = sys.argv[4]
    hst = "localhost"

    conn = MySQLdb.connect(host=hst, port=3306, user=usr, passwd=pw, db=db)
    cur = conn.cursor()

    sql = """SELECT * FROM states WHERE LIKE %s ORDER BY id"""
    cur.execute(sql, (search, ))
    states = cur.fetchall()
    for state in states:
        print(state)
