# Exercise 1: 
# Write a program to calculate net salary for employee.
# Take input for the employee name, number of hours and their hourly rate. 

employee_name = input("enter employee name: ")
employee_hours = input("enter hours worked: ")
employee_rate = input("enter hourly rate: ")

payrate = float(employee_rate)
hours = float(employee_hours)
taxrate = 0.15

grosspay = payrate * hours
withtax = grosspay*taxrate

netpay = grosspay - withtax

print("grosspay:", grosspay)
print("withholding tax:", withtax)
print("netpay:", netpay)