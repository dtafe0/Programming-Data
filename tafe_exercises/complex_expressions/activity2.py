# Modify the program to ask the user for a number and then print the message (the year they’ll turn that number) to the user. (Hint: think about the order of operations in Python).
# Print the messages the number of times specified by the user in ‘a' above, on separate lines. (Hint: use a loop).

from datetime import datetime

age = input("enter your age:")
desired_age = input("enter your desired age:")

years2desired_age = int(desired_age) -int(age)

centurion = datetime.now().year + years2desired_age

print("you will turn age", desired_age, "at the year", centurion)


