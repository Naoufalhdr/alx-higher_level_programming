#!/usr/bin/python3
""" Lists all values where name matches the argument from the database
hbtn_0e_0_usa """
import sys
import MySQLdb


if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", user=arg[1],
                           passwd=arg[2], db=arg[3], port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
                   .format(arg[4]))
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()
