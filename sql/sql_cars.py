# create a  SQLite3 database and table

# import the sqlite3 library
import sqlite3

# create a new table
conn = sqlite3.connect('cars.db')

# get a cursor object to execute SQL commands
cursor = conn.cursor()

# crate a table
cursor.execute('''CREATE TABLE cars
               (make TEXT, model TEXT, quantity INT)''')

# close the database connection
