# Exercise 6:
#  Write code that takes input and declares a variable to represent 
# temperature in Fahrenheit (F). 
# Calculate and display the equivalent temperature in Celsius (C) 
# by applying the following formula: C = (F - 32) * 5 / 9 
#  Display both values.  For example: 
# Fahrenheit: 89.6 
# Celsius: 32 
#  Note: (Use the internet to compare your application result to see if the calculation is correct.)

F = input("Enter Temperature in Fahrenheit: ")

C = (float(F)-32)*5/9

print( "Fahrenheit:", F)
print( "Celsius:", C)