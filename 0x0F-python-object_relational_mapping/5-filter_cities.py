#!/usr/bin/python3
"""Search cities belonging to a state"""

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

    sql = """SELECT cities.id, cities.name
          FROM cities
          INNER JOIN states ON cities.state_id=states.id
          WHERE states.name = %s
          ORDER BY id"""
    cur.execute(sql, (search, ))
    rows = cur.rowcount
    cities = cur.fetchall()
    for i in range(0, len(cities)):
        print(i)
        print(rows)
        if (i < rows - 1):
            print(city[1], end=", ")
        else:
            print(city[1])
