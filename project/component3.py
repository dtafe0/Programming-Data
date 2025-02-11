# 	Component 3 – 
# view existing accounts (displaying users).
# This component displays a numbered list of the existing user
#  accounts (not including their passwords).


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