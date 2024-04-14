#!/usr/bin/python3
import MySQLdb
import sys

usr = sys.argv[1]
pw = sys.argv[2]
db = sys.argv[3]
hst = "localhost"

conn = MySQLdb.connect(host=hst, port=3306, user=usr, passwd=pw, db=db)
cur = conn.cursor()

cur.execute("SELECT * FROM states")
states = cur.fetchall()
for state in states:
    print(state)
