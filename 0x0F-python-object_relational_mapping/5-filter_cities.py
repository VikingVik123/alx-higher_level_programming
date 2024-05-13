#!/usr/bin/python3
""" script  takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database, charset="utf8")
    cursor = connection.cursor()

    try:
        query = ("SELECT cities.name FROM cities INNER JOIN states ON states.id=cities.state_id WHERE states.name=%s", (sys.argv[4],))

        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        connection.close()
