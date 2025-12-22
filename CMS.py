# Dictonary that will hold all of the contacts
user_contacts = {
    'Jessie Castellanos' : {'Phone Number': '999-999-9999', 'email': 'jessie@emailprovider.com'}
}

# TODO: Create an add function. Need to confirm that the information is not the exact same.
def add():
    print('Please give me the name of the contact.')
    contact_name = input('> ')
    if contact_name.replace(" ", "").isalpha() is not True:
        print('This is not a valid name... Try again')
        add()
    else:
        pass
    print('Please give me the contacts phone number. Format should be, xxx-xxx-xxxx')
    contact_number = input ('> ')
    print('Please give me the contacts, email.')
    contact_email = input('> ')
    if contact_name not in user_contacts:
        if contact_name:
            if contact_number:
                if contact_email:
                    user_contacts[contact_name] = {'Phone Number': contact_number, 'email': contact_email}
                    print(contact_name, user_contacts[contact_name])
    else:
        print('User already exists in the database.')
    return None

def view():
    for contact in user_contacts:
        print(contact, user_contacts[contact])
    return None


def search():
    print('Type the name of the contact you\'re looking for.')
    contact_name = input('> ')
    if contact_name in user_contacts:
        print(contact_name, user_contacts[contact_name])
    else:
        print('User could not be found.')
    return None


def edit():
    print('Type the contact that you would like to edit.')
    edit_name = input('> ')
    print('Do you want to update their phone number? yes or no')
    edit_number = input('> ')
    if edit_number == 'yes':
        print('please give me the updated phone number.')
        new_number = input('> ')
        user_contacts[edit_name]['Phone Number'] = new_number
    print('Do you want to update their email address? yes or no')
    edit_email = input('> ')
    if edit_email == 'yes':
        new_email = input('> ')
        user_contacts[edit_name]['email'] = new_email 
    print(edit_name, user_contacts[edit_name])
    return None


def delete():
    print('Type the name of the contact you would like to delete.')
    delete_name = input('> ')
    if delete_name in user_contacts:
        del user_contacts[delete_name]
        print(f"{delete_name} has been removed from the database.")
    return None


def menu():
    options = ['1', '2', '3', '4', '5', '6']
    while True:
        print('What would you like to do? Choose the corresponsing number.')
        print('1. Add a contact', '2. View all contacts', '3. Search contacts', '4. Edit contact', '5. Delete contact', '6. Exit', sep='\n')
        print()
        user_input = input("> ")

        if user_input == '6':
            sys.exit()
        elif user_input == '5':
            delete()
            break
        elif user_input == '4':
            edit()
            break
        elif user_input == '3':
            search()
            break
        elif user_input == '2':
            view()
            break
        elif user_input == '1':
            add()
            break
        elif user_input not in options:
            print('That was not a valid option, please try again.')


"""
1. Add a contact
2. View all contacts
3. Search contacts
4. Edit contact
5. Delete contact

After each step:

* Run the program
* Try to break it intentionally
"""

# TODO: Add Input validation & Error Handling.

# TODO: Add File Peristence.

# TODO: Refactor the code.

if __name__ == '__main__':
    import sys, re
    menu()

