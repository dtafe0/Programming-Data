# 	Simple Menu System – Daniel Ly 11/02/2025
# Create a simple menu system that incorporates the 3 components and will allow the user to:
#     1. Register (Component 1).
#     2. Login (Component 2). 
#     3. View accounts (Component 3). Users must successfully log in (Component 2) before accessing the account listing.
#     4. Exit the program

import sys
import os

# trying to find directory of this script so can open accounts.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "accounts.txt"
file_path = os.path.join(script_dir, file_name)

# define the simple program function
def simple_program(command):

    # declare a globally accessible variable to check if logged in
    global isLoggedin

    # match each input to the correct option
    match command:

        # component 1 - adds a new user login to accounts.txt
        case '1'|'register':
            print('registering....')

             # Get the new username and password
            username = input("input username: ")
            password = input("input password: ")

            # loop input until user enters valid password
            while len(password) < 10 :
                print("password not long enough!")
                password = input("please re-enter password: ")

            # combine username and password into one string
            login = username +","+ password

            # open the accounts.txt file and write login
            with open(file_path, 'a') as file:
                file.write(login + '\n')

            # return result
            return "registered OK\n"
        
        # component 2 - checks accounts.txt for existing login
        case '2'|'login':
            print('logging in.....')

            # kick user back to main menu if already logged in
            try:
                if isLoggedin:
                    return "Already logged in!"
            except NameError:
                print("first time logging in....")

            # Get the current username and password
            username = input("input username: ")
            password = input("input password: ")

            # combine username and password into one string
            login = username +","+ password

            # open the accounts.txt file
            with open(file_path, 'r') as file:
                # read the entire file and return it as a list of strings
                # where each string represents a line from the file
                list = file.readlines()

                # iterate through each line using for loop
                for eachLine in list:

                    # selection using equality operator
                    if eachLine.strip() == login:

                        # user is now logged on
                        isLoggedin = True

                        # return result
                        return "Logged in!"

            # user is not logged on  
            isLoggedin = False      

            # return result
            return "Login not Found!"
        
        # component 3 - checks accounts.txt for existing login
        case '3'|'view accounts':
            print('viewing....')

            # kick user back to main menu if not logged in
            try:
                if not isLoggedin:
                    return "you must be logged in!"
                else:
                    print("isLoggedin is:",isLoggedin)
            except NameError:
                return "you must be logged in!"
            
            with open(file_path, 'r') as file:
                # read the entire file and return it as a list of strings
                # where each string represents a line from the file
                list = file.readlines()

                # iterate through each line using for loop
                for index, eachLine in enumerate(list,start=1):
                    #print(eachLine)
                    print(f"{index}.", eachLine.split(',', 1)[0])

            # return result
            return "OK"
        
        case '4'|'exit':
            print("exiting....")

            # exit the program
            sys.exit()
            return " exit"
        case _:
            return "Unknown command!"

while True:        
    print("\nmenu options:\n1. register\n2. login\n3. view accounts\n4. exit")
    option = input("please pick an option: ")
    print(simple_program(option))