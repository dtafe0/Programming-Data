# Task 02
# Write code that declares a variable named minutes, which holds minutes worked on a job, and assign a value.
# Display the value in hours and minutes; for example:
# 197 minutes becomes 3 hours and 17 minutes.
# Be sure to use a named constant where appropriate.

minutes = 197
hours = minutes // 60
mins = minutes % 60
print(minutes, "minutes becomes", hours, "hrs", mins, "mins")