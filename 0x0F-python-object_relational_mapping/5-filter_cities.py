#!/usr/bin/python3
""" The script takes a state name as input and retrieves all the cities
within that state from the "hbtn_0e_4_usa" database """
import sys
import MySQLdb


if __name__ == "__main__":
    arg = sys.argv
    conn = MySQLdb.connect(host="localhost", user=arg[1],
                           passwd=arg[2], db=arg[3], port=3306)
    cursor = conn.cursor()
    sql_query = (f"SELECT cities.name "
                 f"FROM cities INNER JOIN states "
                 f"ON cities.state_id = states.id "
                 f"WHERE states.name = '{arg[4]}'")
    cursor.execute(sql_query)
    results = ', '.join(city[0] for city in cursor.fetchall())
    print(results)

    cursor.close()
    conn.close()
