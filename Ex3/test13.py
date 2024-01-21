"""
Find the factorial of a given number
Write a program to use the loop to find the factorial 
of a given number.

The factorial (symbol: !) means to multiply all 
whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 x 4 x 3 x 2 x 1 = 120

Expected output: 120

"""


def findFactorial(num):
    if num <= 10000:
        resp = 1
        respStr = []
        for x in range(num, 0, -1):
            resp = resp * x
            respStr.append(str(x))
        result = " x ".join(str(ls) for ls in respStr)
        print(str(num) + "! = ", result, "=", resp)
    else:
        print("Process will take time to finish, aborting operation...")
        print("please enter less than 10000")


findFactorial(int(input("Please enter to find factorial:- ")))
