#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8")
    cursor = connection.cursor()
    cursor.execute(("SELECT * FROM states WHERE name LIKE BINARY '{}'"
        .format(sys.argv[4])))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
