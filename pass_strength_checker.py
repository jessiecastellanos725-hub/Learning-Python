import string, random, itertools

def generate_password():
    options = ['yes', 'no']
    print('Right-O, I will generate a password for you. I do have a few questions.')
    while True:
        print('How long would you like the password to be?')
        pass_length = input('>')
        if pass_length.lower() == '':
            print('That is not an option.')
        else:
            break
    while True:    
        print('Would you like lower case characters? Yes or No')
        lower_input = input('>')
        if lower_input.lower() not in options:
            print('That is not an option.')
        else:
            break
    while True:    
        print('Would you like upper case characters? Yes or No ')
        upper_input = input('>')
        if upper_input.lower() not in options:
            print('That is not an option.')
        else:
            break
    while True:
        print('Would you like numbers? Yes or No')
        numbers_input = input('>')
        if numbers_input.lower() not in options:
            print('That is not an option.')
        else:
            break
    while True:
        print('Would you like to use special characters?')
        special_input = input('>')
        if special_input.lower() not in options:
            print('That is not an option.')
        else:
            break

    #List to capture all the different characters
    char_options = []
    if lower_input.lower() == 'yes':
        char_options.append(string.ascii_lowercase)
    elif lower_input.lower() == 'no':
        pass
    if upper_input.lower() == 'yes':
        char_options.append(string.ascii_uppercase)
    elif upper_input.lower() == 'no':
        pass
    if numbers_input.lower() == 'yes':
        char_options.append(string.digits)
    elif numbers_input.lower() == 'no':
        pass
    if special_input.lower() == 'yes':
        char_options.append(string.punctuation)
    elif special_input.lower() == 'no':
        pass
    char_joined = list(itertools.chain.from_iterable(char_options))
    password = ''
    for i in range(int(pass_length)):
        password += random.choice(char_joined)

    print(password)


# Checks the minimum length of the password.
def min_length(input):
    if len(input) < 8:
        return False
    else:
        return True

def upper_case(input):
    upper = any(char.isupper() for char in input)

    if upper:
        return True
    else:
        return False

def lower_case(input):
    lower = any(char.islower() for char in input)

    if lower:
        return True
    else:
        return False
    

def numbers(input):
    number = any(char.isdigit() for char in input)

    if number:
        return True
    else:
        return False

def special(input):
    unique = any(char in string.punctuation for char in input)

    if unique:
        return True
    else:
        return False

def password_check(min_length, upper_case, lower_case, numbers, special):
    password_strength = 0
    if min_length:
        print('Password length is at least 8 characters.')
        password_strength += 20
    else:
        print('Your password should be atleast 8 characters in length.')
    
    if upper_case:
        print('Password has a uppercase character.')
        password_strength += 20
    else:
        print('Your password should have a uppercase character.')
    
    if lower_case:
        print('Password has a lowercase character.')
        password_strength += 20
    else:
        print('Your password should have a lowercase character.')

    if numbers:
        print('Password has a number.')
        password_strength += 20
    else:
        print('Your password should have a number.')

    if special:
        print('Password has a special character.')
        password_strength += 20
    else:
        print('Your password should have a special character.')
    
    print(f'Your password has a score of {password_strength}/100. Please review my previous feed back to determine what to add.')

    with open('common_pass.txt', 'r') as f:
        my_list = [line.strip() for line in f]
    
    if user_input in my_list:
        print('You should not use this password as it is a common password')
    else:
        print('This password is not common!')
    
if __name__ == '__main__':
    print('Do you want me to generate a password for you or would you like for me to check a password that you want to use. Type 1 for generate and 2 for validate')
    choice = input('>')
    if choice == '2':
        print('Please enter the password that you would like to use')
        user_input = input('>')
        password_check(min_length(user_input), upper_case(user_input), lower_case(user_input), numbers(user_input), special(user_input))
    elif choice == '1':
        generate_password()
