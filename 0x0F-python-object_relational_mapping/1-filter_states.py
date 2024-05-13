#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")

    # Create cursor
    cursor = connection.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY name")

    # Fetch all rows
    rows = cursor.fetchall()

    # Display results
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    connection.close()
