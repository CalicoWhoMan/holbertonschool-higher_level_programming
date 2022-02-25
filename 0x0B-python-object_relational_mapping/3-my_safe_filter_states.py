#!/usr/bin/python3
"""Script like #2; but make it safe from MySQL injections"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], database=sys.argv[3])
    mem = db.cursor()
    mem.execute("""SELECT * FROM states WHERE name = '{}'
    ORDER BY states.id ASC""".format(sys.argv[4].split()[0]))

    for row in mem.fetchall():
        print(row)

    mem.close()
    db.close()
