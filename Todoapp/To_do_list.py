import sqlite3, logging
from datetime import date

# Configuring basic logging system.
logging.basicConfig(level=logging.INFO)

# Building the connection to the database.
conn = sqlite3.connect('todolist.db', isolation_level=None) 
c = conn.cursor()

# Creating Table
c.execute('CREATE TABLE IF NOT EXISTS tasks (task TEXT, priority_level TEXT, due_date TEXT, completion_status TEXT, date_created TEXT) STRICT')

# Testing Table
logging.info(c.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall())

# Commit changes
conn.commit()
logging.info("Data inserted successfully")


# TODO: Add task to database function
def add_task():
    print('Please describe the task.')
    describe_task = input('> ')
    print('Please assign a priority, urgent, high, medium or low.')
    priority = input('> ')
    print('Please provide a due date for this task. YYYY-MM-DD Format.')
    due_date = input('> ')
    try:
        c.execute('INSERT INTO tasks VALUES(?,?,?,?,?)',[describe_task, priority, due_date, "Not Complete", date.now()])
        conn.commit()
        logging.info("Record inserted successfully.")
    except sqlite3.error as e:
        print(f"Failed to insert record: {e}")
        if c:
            c.rollback()


# TODO: View all tasks function
def view_all_tasks():
    for row in (c.execute('SELECT rowid, * FROM tasks').fetchall()):
        print('Row data:', row)

# TODO: View pending tasks
def pending_tasks():
    for row in (c.execute('SELECT rowid, * FROM tasks WHERE completion_status = "Not Complete"').fetchall()):
        print('Row data:', row)

# TODO: Mark task complete function
def mark_complete():
    pass

# TODO: Delete Task function
def delete_task():
    print('Please choose the row id of the task that you want deleted.')
    delete_input = input("> ")
    c.execute(f'DELETE FROM tasks WHERE rowid={delete_input}')
    logging.info('Task deleted.')

# TODO: Menu to choose
def menu():
    while True:
        print("Please tell me what you would like to do.", "1. Add new task.", "2. View all tasks.", "3. Mark a task complete.", "4. Delete a task.", "5. View all pending tasks.")
        user_choice = input('> ')
        if user_choice == "1":
            add_task()
            break
        elif user_choice == "2":
            view_all_tasks()
            break
        elif user_choice == "3":
            mark_complete()
            break
        elif user_choice == "4":
            delete_task()
            break
        elif user_choice == "5":
            pending_tasks()
            break
        else:
            print("That is not a valid choice, please try again.")


if __name__ == "__main__":
    menu()
