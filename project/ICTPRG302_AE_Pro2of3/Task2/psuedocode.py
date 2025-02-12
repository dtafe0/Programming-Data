# Component 2 -
# checking a username and password (logging in).
# This component takes an existing username and password (for a previously registered user)
# and checks if they match a valid entry in the file (accounts.txt).
# assumes login is stored in the plaintext format "username,password"

# Get the current username and password
username = input("input username: ")
password = input("input password: ")

# combine username and password into one string
login = username +","+ password

# set flag to show login state
valid_entry = False

# open the accounts.txt file
file = open("accounts.txt", "r")

# check if the file is opened in read only mode
if file.mode == 'r':

    # read the entire file and return it as a list of strings
    # where each string represents a line from the file
    list = file.readlines()

    # iterate through each line using for loop
    for eachLine in list:

        # selection using equality operator
        if eachLine.strip() == login:

            # set flag for valid entry to true
            valid_entry = True

            # exit the loop
            break

    # show the result to the user
    print("login for", username, "is", valid_entry)

# close file
file.close()