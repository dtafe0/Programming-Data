# Task 06
# (Compute the volume of a cylinder) Write a program that reads in the radius and length of a cylinder and computes the area and volume using the following formulas:
# Area = radius * radius * π
# (In order to obtain the value of π you will need to use math.pi from the math module)
# Volume = area * length
# Here is a sample run:
# Given that the radius and length of a cylinder are 5.5 and 12 respectively, the output of the code should be:
# The area is: 95.0331
# The volume is: 1140.4

import math

rad = input("enter radius:")
len = input("enter length:")

area = float(rad) * float(rad)* math.pi
vol = float(area) * float(len) 

print("The area is:", area)
print("The volume is:", vol)