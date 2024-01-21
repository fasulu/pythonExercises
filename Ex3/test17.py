"""
Find the sum of the series upto n terms
Write a program to calculate the sum of series up to n term. 
For example, if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690

Given: n = 5
Expected output: 24690

"""


def sumOfSeries(num):
    result = 0
    for x in range(1, num + 1):
        result = result + int((str(2) * x))  # to print a string several time ('Hi'*5)
    return result


print(sumOfSeries(5))
