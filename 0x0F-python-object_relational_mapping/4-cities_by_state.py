#!/usr/bin/python3
""" script that  lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8")
    cursor = connection.cursor()

    try:
        cursor.execute("SELECT * FROM cities ORDER BY id ASC")
        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print("Error:", e)
    finally:
        cursor.close()
        connection.close()
