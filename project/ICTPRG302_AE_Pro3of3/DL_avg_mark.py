# Daniel Ly 14/02/2025
# This program determines the average mark for a student
# based on their marks from five different subjects

# define a function that loops until a valid mark is entered
def getvalidmark(prompt):
    while True:
        value = input(prompt)
        try:
            # make sure mark is an integer
            mark = round(float(value))
            # set boundaries for mark
            if 0 <= mark <= 100:
                return mark
            else:
                print(mark, "is not a valid mark!")
        except ValueError:
            print(value, "is not a valid mark!")


print("please enter your 5 marks below")

#read 5 inputs
mark1 = getvalidmark("enter mark 1: ")
mark2 = getvalidmark("enter mark 2: ")
mark3 = getvalidmark("enter mark 3: ")
mark4 = getvalidmark("enter mark 4: ")
mark5 = getvalidmark("enter mark 5: ")

#create array/list with five marks
marksList = [mark1, mark2, mark3, mark4, mark5]

#print the array/list
print(marksList)

#calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList)/5

#display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))