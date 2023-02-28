#!/usr/bin/python3
""" Task 0 """
import sys
import MySQLdb


if __name__ == "__main__":
    """ Prints states from database hbtn_0e_0_usa """
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states")
    [print(state) for state in c.fetchall()]