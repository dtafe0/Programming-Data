# Task 03
# Write code that declares variables to represent a user’s hourly rate of pay and the number of hours worked.
# Assign appropriate values to the variables, then calculate and display the user’s gross pay for a week, the withholding tax (15% of gross pay), and the net pay (gross pay – withholding). An example output would be:
# Gross Pay: 1500
# Withholding Tax: 225
# Net Pay: 1275

payrate = 42
hours = 37.5
taxrate = 0.15


grosspay = payrate * hours
withtax = grosspay*taxrate

netpay = grosspay - withtax

print("grosspay:", grosspay)
print("withholding tax:", withtax)
print("netpay:", netpay)