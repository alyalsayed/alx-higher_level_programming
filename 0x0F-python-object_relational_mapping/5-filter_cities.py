#!/usr/bin/python3
"""lists all cities of that state using htbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    curs = db.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
        FROM cities JOIN states ON cities.state_id = states.id \
        WHERE states.name = '{}';".format(sys.argv[4]))
    states = curs.fetchall()

    for state in states:
        print(", ".join([state[1]]))
