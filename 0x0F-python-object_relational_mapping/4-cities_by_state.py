#!/usr/bin/python3
"""Module for Task 4"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name FROM
                    cities INNER JOIN states ON states.id=cities.state_id""")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
