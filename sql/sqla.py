# create a SQLite3 database and table


# import the sqlite3 library
import sqlite3

# Create a new table if it doesn't exist
conn = sqlite3.connect('new.db')

# Get a cursor object to execute SQL commands
cursor = conn.cursor()

# create a table
cursor.execute('''CREATE TABLE population
                (city TEXT, state TEXT, population INT)''')

# close the database connection

conn.close()
