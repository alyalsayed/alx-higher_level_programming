#!/usr/bin/python3
"""Lists all states with a name starting with N from
hbtn_0e_0_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)
    curs = db.cursor()
    curs.execute("SELECT * FROM states ORDER BY id;")
    states = curs.fetchall()

    for state in states:
        if state[1][0] == "N":
            print(state)
