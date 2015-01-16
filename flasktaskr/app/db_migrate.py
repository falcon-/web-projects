# db_migrate.py


from views import db
from datetime import datetime
from config import DATABASE_PATH
import sqlite3

with sqlite3.connect(DATABASE_PATH) as connection:

    # get a cursor object used to execute SQL commands
    cursor = connection.cursor()

    # temporarily change the name of tasks table
    cursor.execute("""ALTER TABLE tasks RENAME TO old_tasks""")

    # recreate a new tasks table with updated schema
    db.create_all()

    # retrieve data from old_tasks table
    cursor.execute("""SELECT name, due_date, priority, status
    FROM old_tasks ORDER BY task_id ASC""")

    # save all rows as a list of tuples; set posted_date to now and
    # user_id to 1
    data = [(row[0], row[1], row[2], row[3],
             datetime.now(), 1) for row in cursor.fetchall()]

    # delete old_tasks table
    cursor.execute("DROP TABLE old_tasks")
