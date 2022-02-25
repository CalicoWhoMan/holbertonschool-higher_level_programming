#!/usr/bin/python3
"""Script that takes the state as arg and lists all 'cities' of that state"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                    passwd=sys.argv[2], database=sys.argv[3])
    mem = db.cursor()
    mem.execute("""SELECT cities.name FROM states
    JOIN cities ON cities.state_id = states.id WHERE states.name = '{}'
    ORDER BY states.id ASC""".format(sys.argv[4]))

    for row in mem.fetchall():
        print(row)

    mem.close()
    db.close()
