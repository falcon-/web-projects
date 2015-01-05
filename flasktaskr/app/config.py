'''config.py'''

import os

#Qgrabs the folder where the script runs
BASEDIR = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'flasktaskr.db'
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'my_precious'

# defines the full path for the database
DATABASE_PATH = os.path.join(BASEDIR, DATABASE)
