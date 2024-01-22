"""
Create a function with a default argument
Write a program to create a function show_employee() 
using the following conditions.

It should accept the employee's name and salary and display 
both.If the salary is missing in the function call then 
assign default value 9000 to salary

Given:
showEmployee("Ben", 12000)
showEmployee("Jessa")

Expected output:
Name: Ben salary: 12000
Name: Jessa salary: 9000

"""


# Method one
def showEmployee(name, sal=None):
    name = name
    sal = sal or ""

    if name != "" and sal != "":
        print(f"Name: {name}, salary: {sal}")
    elif name != "" and sal == "":
        print(f"Name: {name}, salary: 9000")


# Method two
def showEmployee1(*args):
    name, sal = "", 0
    if len(args) == 2:
        name = args[0]
        sal = args[1]
    elif len(args) == 1:
        name = args[0]
        sal = 9000

    if name != "" and sal != "":
        print(f"Name: {name}, salary: {sal}")


showEmployee("Ben", 12000)
showEmployee("Jessa")


showEmployee1("Ben", 12000)
showEmployee1("Jessa")
