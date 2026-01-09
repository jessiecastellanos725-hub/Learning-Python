import string

print('Please enter the password that you would like to use')
user_input = input('>')


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
    password_check(min_length(user_input), upper_case(user_input), lower_case(user_input), numbers(user_input), special(user_input))