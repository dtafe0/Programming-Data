# Task 05
# Travel Tickets Company sells tickets for airlines, tours, and other travel-related services. Because ticket agents frequently mistype long ticket numbers, Travel Tickets has asked you to write an application that indicates invalid ticket number entries.
# In your code declare a variable to hold a six-digit ticket number. Ticket numbers are designed so that if you drop the last digit of the number, then divide the number by 7, the remainder of the division will be identical to the last dropped digit. This process is illustrated in the following example:
# a. Assign a value for the ticket number; for example, 123454.
# b. Remove the last digit, leaving 12345.
# c. Determine the remainder when the ticket number is divided by 7. In this case, 12345 divided by 7 leaves a remainder of 4.
# d. Assign the Boolean value of the comparison between the remainder and the digit dropped from the ticket number. To compare two values, use the == symbol (double equals).
# e. Display the result - true or false –
# Test the application with the following ticket numbers:
# • 123454; the comparison should evaluate to true
# • 147103; the comparison should evaluate to true
# • 154123; the comparison should evaluate to false

tn = str(147103)

a = int(tn[:-1]) % 7 

print(a)
print(tn[5])
print(a==int(tn[5]))

