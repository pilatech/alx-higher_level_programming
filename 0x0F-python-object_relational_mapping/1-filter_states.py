#!/usr/bin/python3
"""Print list of states that start with N from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    hst = "localhost"

    conn = MySQLdb.connect(host=hst, port=3306, user=usr, passwd=pw, db=db)
    cur = conn.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    states = cur.fetchall()
    for state in states:
        print(state)
