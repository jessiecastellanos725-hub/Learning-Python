import sqlite3, logging, sys
from datetime import date, datetime

# Configuring basic logging system.
logging.basicConfig(level=logging.INFO)

# Building the connection to the database.
conn = sqlite3.connect('todolist.db', isolation_level=None) 
c = conn.cursor()

# Creating Table
c.execute('CREATE TABLE IF NOT EXISTS tasks (task TEXT, priority_level TEXT, due_date TEXT, completion_status TEXT, date_created TEXT) STRICT')

# Testing Table
logging.info(c.execute('SELECT name FROM sqlite_schema WHERE type="table"').fetchall())

# Validation for the date string.
def validate_date(date_string):
    try:
        datetime.strptime(date_string, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# TODO: Add task to database function
def add_task():
    while True:
        print('Please describe the task.')
        describe_task = input('> ')
        print('Please assign a priority, urgent, high, medium or low.')
        priority = input('> ')
        print('Please provide a due date for this task. YYYY-MM-DD Format.')
        due_date = input('> ')
        if validate_date(due_date):
            if priority in priority_levels:
                try:
                    c.execute('INSERT INTO tasks VALUES(?,?,?,?,?)',[describe_task, priority, due_date, "Not Complete", date.today()])
                    logging.info("Record inserted successfully.")
                    break
                except sqlite3.Error as e:
                    print(f"Failed to add new record: {e}")
            else:
                print('The priority level is not correct.')
        else:
            print('The calendar date format is incorrect.')


# TODO: View all tasks function
def view_all_tasks():
    if c.execute('SELECT rowid, * FROM tasks').fetchall() == []:
        print('No tasks currently...')
    else:
        try:
            for row in (c.execute('SELECT rowid, * FROM tasks').fetchall()):
                print(f'ID: {row[0]}, Task: {row[1]}, Priority: {row[2]}, Due Date: {row[3]}, Status: {row[4]}, Created date{row[5]}')
        except sqlite3.Error as e:
            print(f"Failed to retrieve records: {e}")
        

# TODO: View pending tasks
def pending_tasks():
    if c.execute('SELECT rowid, * FROM tasks WHERE completion_status = "Not Complete" ORDER BY priority').fetchall() == []:
        print('There are not pending tasks...')
    else:
        try:
            for row in (c.execute('SELECT rowid, * FROM tasks WHERE completion_status = "Not Complete" ORDER BY priority').fetchall()):
                print(f'ID: {row[0]}, Task: {row[1]}, Priority: {row[2]}, Due Date: {row[3]}, Status: {row[4]}, Created date{row[5]}')
        except sqlite3.Error as e:
            print(f"Failed to retrieve pending tasks: {e}")
        

# TODO: Mark task complete function
def mark_complete():
    print('Please give me the task ID that you would like to mark as complete.')
    complete_input = input('> ')
    if not complete_input.isdigit():
        print('Invalid ID. Must be a number.')
        return
    else:
        try:
            c.execute('UPDATE tasks SET completion_status = "Complete" WHERE rowid =?', (complete_input,))
            logging.info("Marked the task as complete.")
        except sqlite3.Error as e:
            print(f"Failed to mark complete: {e}")

# TODO: Delete Task function
def delete_task():
    print('Please choose the row id of the task that you want deleted.')
    delete_input = input("> ")
    if delete_input.isdigit():
        try:
            c.execute('DELETE FROM tasks WHERE rowid=?', (delete_input,))
            logging.info('Task deleted.')
        except sqlite3.Error as e:
            print(f"Failed to delete record: {e}")
    elif not delete_input.isdigit():
        print('Invalid ID. Must be a number')
            


# TODO: Menu to choose
def menu():
    while True:
        print("Please tell me what you would like to do.", "1. Add new task.", "2. View all tasks.", "3. Mark a task complete.", "4. Delete a task.", "5. View all pending tasks.", "6. Exit.")
        user_choice = input('> ')
        if user_choice == "1":
            add_task()
            
        elif user_choice == "2":
            view_all_tasks()
            
        elif user_choice == "3":
            mark_complete()
            
        elif user_choice == "4":
            delete_task()
            
        elif user_choice == "5":
            pending_tasks()
            
        elif user_choice == '6':
            conn.close()
            sys.exit()
        else:
            print("That is not a valid choice, please try again.")


if __name__ == "__main__":
    priority_levels = ['urgent', 'high', 'medium', 'low']
    menu()
