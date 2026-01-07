import ipaddress

print('Please provide me with an IP address that you want me to check.')
user_input = input('> ')

def validate_ip_address(ip_address):
    try:
        if ipaddress.ip_address(ip_address):
            print('That is a valid IP address.')
    except ValueError as e:
        print(f"{e}")

def is_private(ip_address):
    try:
        if ipaddress.IPv4Address(ip_address).is_private:
            print('This is a private IP address.')
    except ValueError as e:
        print(f"{e}")

def is_multicast(ip_address):
    try:
        if ipaddress.IPv4Address(ip_address).is_multicast:
            print('This is a multicast IP address.')
    except ValueError as e:
        print(f"{e}")

def is_public(ip_address):
    try:
        if ipaddress.IPv4Address(ip_address).is_global:
            print('This is a public IP address.')
    except ValueError as e:
        print(f"{e}")

def is_loopback(ip_address):
    try:
        if ipaddress.IPv4Address(ip_address).is_loopback:
            print('This is a loopback ip address.')
    except ValueError as e:
        print(f"{e}")




if __name__ == '__main__':
    validate_ip_address(user_input)
    is_private(user_input)
    is_loopback(user_input)
    is_public(user_input)
    is_multicast(user_input)