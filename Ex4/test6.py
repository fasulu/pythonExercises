"""
Create a recursive function
Write a program to create a recursive function to calculate 
the sum of numbers from 0 to 10.

A recursive function is a function that calls itself again 
and again.

Expected Output:

55

"""


def recursiveFunc(num):
    print(num)
    if num:       # when reaches 0 (means False) goes to else
        return num + recursiveFunc(num - 1) # calling same function by reducing number by 1
    else:
        return 0


cnt = 0
num = recursiveFunc(10)
print(num)
