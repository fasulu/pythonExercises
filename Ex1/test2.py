"""
Print the sum of the current number and the previous number
Write a program to iterate the first 10 numbers, and in each 
iteration, print the sum of the current and previous number.

Printing current and previous number sum in a range(10)
Current Number 0 Previous Number  0  Sum:  0
Current Number 1 Previous Number  0  Sum:  1
Current Number 2 Previous Number  1  Sum:  3
Current Number 3 Previous Number  2  Sum:  5

"""


def sumIteration(num):
    print("Printing current and previous number sum in a range(" + str(num) + ")")
    for x in range(num):
        preNum = 0 if x == 0 else x - 1
        print(
            "Current Number "
            + str(x)
            + " Previous Number"
            + str(x)
            + " Sum: "
            + str(preNum + x)
        )


sumIteration(10)
