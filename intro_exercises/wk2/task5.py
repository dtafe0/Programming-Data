# Exercise 5:
#  Write code that takes inputs for a variable named minutes,
#  which holds minutes worked on a job, and assign a value.
# Output the value in hours and minutes; for example: 
#  197 minutes becomes 3 hours and 17 minutes. 

minutes = 197
hours = minutes // 60
mins = minutes % 60
print(minutes, "minutes becomes", hours, "hrs", mins, "mins")