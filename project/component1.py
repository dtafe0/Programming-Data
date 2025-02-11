# 	Component 1 – 
# creating a new user account (registration).
# This component takes a new username and password from the
# user and appends them to the existing file (accounts.txt). 
# The user can choose their password with a mixture of 
# characters, but the password must be checked to ensure 
# it meets minimum length requirements.

# Get the current username and password
username = input("input username: ")
password = input("input password: ")

# combine username and password into one string
login = username +","+ password

# set flag to show login state
valid_entry = False

# open the accounts.txt file
file = open("accounts.txt", "a")


    print("login for", username, "is", valid_entry)

# close file
file.close()