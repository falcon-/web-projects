# UPDATE and DELETE statements

import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

    # update data
    c.execute("UPDATE cars SET quantity= 90 WHERE "
    "model='Mustang'")

    c.execute("UPDATE cars SET quantity= 70 WHERE "
    "model='Accord'")

    print("\nNEW DATA:\n")
    c.execute("SELECT * FROM cars")

    rows = c.fetchall()

    for r in rows:
       print (r[0], r[1], r[2])
