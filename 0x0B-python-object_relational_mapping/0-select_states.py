#!/usr/bin/python3
"""Lists all 'states' from the database"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                    passwd=sys.argv[2], database=sys.argv[3])
    mem = db.cursor()
    mem.execute("SELECT * FROM states ORDER BY states.id ASC")

    for row in mem.fetchall():
        print(row)
        
    mem.close()
    db.close()

