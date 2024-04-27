#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb


if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", user=arg[1],
                           passwd=arg[2], db=arg[3], port=3306)
    cursor = conn.cursor()
    sql_query = (f"SELECT cities.id, cities.name, states.name "
                 f"FROM cities INNER JOIN states "
                 f"ON cities.state_id = states.id")
    cursor.execute(sql_query)
    results = cursor.fetchall()
    for row in results:
        print(row)
    cursor.close()
    conn.close()
