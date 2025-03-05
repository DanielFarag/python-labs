import os
import re
from modules.db import login, register, authenticated


def loginForm():
    os.system('clear')
    while True:
        email=input("Email: ")
        password=input("Password: ")
        auth, user = login(email, password)

        if auth:
            authenticated(user)

            break
        else:
            os.system('clear')

            print("Please enter a valid email and password.")
            continue



def registerForm():
    os.system('clear')
    while True:
        first_name = input(f"First Name: ") 
        if re.fullmatch(r'[A-Za-z]{1,10}', first_name):
            break
        print("Invalid first name. (1-10 char).")

    while True:
        last_name = input(f"Last Name: ") 
        if re.fullmatch(r'[A-Za-z]{1,10}', last_name):
            break
        print("Invalid first name. (1-10 char).")

    while True:
        email = input(f"Email: ") 
        if re.fullmatch(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', email):
            break
        print("Invalid email format. Example: example@email.com")

    while True:
        password = input(f"Password: ")
        if re.fullmatch(r'.{8,}', password):
            break
        print("Invalid password. Must be at least 8 characters.")

    while True:
        confirm_password = input(f"Confirm Password: ")
        if confirm_password == password:
            break
        print("Passwords do not match. Please try again.")

    while True:
        mobile = input(f"Mobile Phone : ")
        if re.fullmatch(r'^(01[0125])\d{8}$', mobile):
            break
        print("Invalid mobile number. Must be a valid Egyptian number (e.g., 01012345678).")


    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "mobile_phone": mobile
    }

    _user = register(user)
    authenticated(_user)


    