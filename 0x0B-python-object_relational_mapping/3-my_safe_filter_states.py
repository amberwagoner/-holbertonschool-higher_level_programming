#!/usr/bin/python3
""" Task 3 """
import sys
import MySQLdb


if __name__ == "__main__":
    """ All values in states where name matches & is safe from injections """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall() if state[1] == sys.argv[4]]
