# Exercise 4:
# Write a program to calculate the area and volume of a cylinder. 
# Take inputs for the appropriate variables.

import math

rad = input("enter radius:")
len = input("enter length:")

area = float(rad) * float(rad)* math.pi
vol = float(area) * float(len) 

print("The area is:", area)
print("The volume is:", vol)