# 	Component 3 – Daniel Ly 11/02/2025
# view existing accounts (displaying users).
# This component displays a numbered list of the existing user
#  accounts (not including their passwords).

import os
# trying to find directory of this script so can open accounts.txt
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = "accounts.txt"
file_path = os.path.join(script_dir, file_name)

# open the accounts.txt file
with open(file_path, 'r') as file:
    # read the entire file and return it as a list of strings
    # where each string represents a line from the file
    list = file.readlines()

    # iterate through each line using for loop
    for index, eachLine in enumerate(list,start=1):
        #print(eachLine)
        print(f"{index}.", eachLine.split(',', 1)[0])
