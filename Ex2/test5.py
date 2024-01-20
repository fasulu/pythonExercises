"""
Accept a list of 5 float numbers as an input from the user
Refer:

Take list as a input in Python.
Python list

Expected Output: [78.6, 78.6, 85.3, 1.2, 3.5]

"""


# def isNaN(num):
#     flag = isinstance(num, float)
#     return flag

lst = []

for x in range(5):
    inputStr = float(input("Please enter float number:- "))
    lst.append(inputStr)

print(lst)


# flag = isNaN(inputStr)
