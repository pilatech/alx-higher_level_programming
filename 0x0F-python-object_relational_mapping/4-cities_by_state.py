#!/usr/bin/python3
"""Print list of cities from the database"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    usr = sys.argv[1]
    pw = sys.argv[2]
    db = sys.argv[3]
    hst = "localhost"

    conn = MySQLdb.connect(host=hst, port=3306, user=usr, passwd=pw, db=db)
    cur = conn.cursor()

    sql = """SELECT cities.id, states.name, cities.name
          FROM cities
          INNER JOIN states ON cities.state_id=states.id
          ORDER BY id"""
    cur.execute(sql)
    states = cur.fetchall()
    for state in states:
        print(state)
