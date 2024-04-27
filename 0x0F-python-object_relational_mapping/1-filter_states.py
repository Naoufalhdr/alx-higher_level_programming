#!/usr/bin/python3
""" Lists all states with a name starting with N  from
the database hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", user=arg[1],
                           passwd=arg[2], db=arg[3], port=3306)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM states WHERE name
                   LIKE BINARY 'N%' ORDER BY id""")
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()
