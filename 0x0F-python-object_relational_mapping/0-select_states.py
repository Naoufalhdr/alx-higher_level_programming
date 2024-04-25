#!/usr/bin/python3

import sys
import MySQLdb

arg = sys.argv
conn = MySQLdb.connect(host="localhost", user=arg[1], passwd=arg[2], db=arg[3])

cursor = conn.cursor()

cursor.execute("SELECT * FROM states")

results = cursor.fetchall()

for row in results:
    print(row)

cursor.close()
conn.close()
