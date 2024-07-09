from dbclone import *

def reg():
    global first_name = str(input("Enter your first name\n>> "))
    last_name = str(input("Enter your last name\n>> "))
    other_name = str(input("Enter your other name\n>> "))
    username = str(input("Enter your username\n>> "))
    email = str(input("Enter your email\n>> "))
    password = str(input("Enter your password\n>> "))
    password1 = str(input("Confirm your password\n>> "))
    country_code = int(input("Select your country:\n1. Nigeria\n2. Benin\n3. Togo\n4. Ghana\n>> "))
    if country_code == 1:
        number = input("Enter your phone number\n>> ")
        phone_number = f'+234{number}'
    elif country_code == 2:
        number = input("Enter your phone number\n>> ")
        phone_number = f'+229{number}'
    elif country_code == 3:
        number = input("Enter your phone number\n>> ")
        phone_number = f'+228{number}'
    elif country_code == 4:
        number = input("Enter your phone number\n>> ")
        phone_number = f'+233{number}'
    else:
        print('Oops! You are not allowed to create an account from your country.')
    address = str(input("Enter your address\n>> "))
    nin = str(input("Enter your NIN number\n>> "))
    return 

reg()

print(create_users(
    first_name,
    last_name,
    other_name,
    username,
    email,
    password1,
    phone_number,
    number,
    address,
    nin
))