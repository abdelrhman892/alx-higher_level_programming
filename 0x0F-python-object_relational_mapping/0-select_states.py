#!/usr/bin/python3
import sys
import MySQLdb

conn = MySQLdb.connect(
    host="localhost",
    user=sys.argv[1],
    passwd=sys.argv[2],
    database=sys.argv[3]
)
cursor = conn.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
for state in cursor.fetchall():
    print(state)

cursor.close()
conn.close()
