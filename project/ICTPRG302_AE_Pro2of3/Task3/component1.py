# 	Component 1 – Daniel Ly 11/02/2025
# creating a new user account (registration).
# This component takes a new username and password from the
# user and appends them to the existing file (accounts.txt). 
# The user can choose their password with a mixture of 
# characters, but the password must be checked to ensure 
# it meets minimum length requirements.

import os
# trying to find directory of this script so can open accounts.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "accounts.txt"
file_path = os.path.join(script_dir, file_name)

# Get the current username and password
username = input("input username: ")
password = input("input password: ")

# loop input until user enters valid password
while len(password) < 10 :
    print("password not long enough!")
    password = input("please re-enter password: ")

# combine username and password into one string
login = username +","+ password

# open the accounts.txt file
with open(file_path, 'a') as file:
    file.write(login + '\n')

