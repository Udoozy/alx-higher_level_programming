#!/usr/bin/python3
"""Module for Task 2"""
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
    search_pattern = sys.argv[4]
    cursor.execute("SELECT * FROM states WHERE name
                   LIKE %s", (search_pattern, ))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
