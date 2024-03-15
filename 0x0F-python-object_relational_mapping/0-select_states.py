#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)
        cursor = db.cursor()

        # Execute the query to select all states
        query = "SELECT * FROM states ORDER BY id ASC"
        cursor.execute(query)

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

        # Close cursor and database connection
        cursor.close()
        db.close()
