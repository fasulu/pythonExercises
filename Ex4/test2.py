"""
Create a function with variable length of arguments
Write a program to create function func1() to accept a 
variable length of arguments and print their value.

Note: Create a function in such a way that we can pass 
any number of arguments to this function, and the function 
should process them and display each argument’s value.

Function call:

call function with 3 arguments
func1(20, 40, 60)

call function with 2 arguments
func1(80, 100)

Expected Output:
Printing values
20
40
60

Printing values
80
100

"""


def func1(*args):
    print("Printing values")
    for val in args:
        print(val)


func1(20, 40, 60)
func1(80, 100)
func1("home", "Documents", "python", "Exercises", "Ex4")
