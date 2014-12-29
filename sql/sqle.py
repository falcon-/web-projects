# INSERT Command with Error Handler


# import the sqlite3 library
import sqlite3

# create the connection object
conn = sqlite3.connect("cars.db")

# get a cursor object used to execute SQL commands
cursor = conn.cursor()

try:
    # insert data
    cursor.execute("INSERT INTO cars VALUES('Ford',"
                   "'Focus',   82)")
    cursor.execute("INSERT INTO cars VALUES('Ford',"
                   "'Mustang',   80)")
    cursor.execute("INSERT INTO cars VALUES('Ford',"
                   "'Escape',   88)")
    cursor.execute("INSERT INTO cars VALUES('Honda',"
                   "'Accord',   88)")
    cursor.execute("INSERT INTO cars VALUES('Honda',"
                   "'Civc',   98)")


    # commit the changes
    conn.commit()
except sqlite3.OperationalError:
    print("Oops!  Something went wrong. Try again...")

# close the database connection
conn.close()
