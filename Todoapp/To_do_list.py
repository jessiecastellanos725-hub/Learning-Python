import sqlite3, logging

# Configuring basic logging system.
logging.basicConfig(level=logging.INFO)

# Building the connection to the database.
conn = sqlite3.connect('todolist.db', isolation_level=None) 
c = conn.cursor()

# Creating Table
c.execute('CREATE TABLE IF NOT EXISTS tasks (task TEXT, priority_level TEXT, due_date TEXT, completion_status TEXT, date_created TEXT) STRICT')

# Testing Table
logging.info(c.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall())