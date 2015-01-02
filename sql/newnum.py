#import sqlite3#
import sqlite3
import random

#establish connection and create newnum.db database#
with sqlite3.connect("newnum.db") as connection:
    #open a cursor to execute cmmands#
    c = connection.cursor()

    """create table, 'numbers', with value 'num' as an integer(the DROP TABLE
    command willl remove the entire table if it exists so we can create a)ew
    one):"""
    c.execute("DROP TABLE if exists numbers")
    c.execute("CREATE TABLE numbers(num int)")

    #use a for loop to insert 100 random values(0 to 100)#
    for i in range(100):
        c.execute("INSERT INTO numbers VALUES(?)",(random.randint(0,100),))
