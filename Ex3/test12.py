"""
Display Fibonacci series up to 10 terms
The Fibonacci Sequence is a series of numbers. 
The next number is found by adding up the two numbers 
before it. The first two numbers are 0 and 1.

Fibonacci sequence:- 0, 1, 1, 2, 3, 5, 8, 13, 21. 
The next number in this series above is 13+21 = 34.

Expected output: 0  1  1  2  3  5  8  13  21  34

"""


def fibonacciSeq(num):
    lst = []
    firstNum = 0
    secondNum = 1
    resp = 0
    lst.append(firstNum)
    lst.append(secondNum)
    for x in range(num):
        resp = firstNum + secondNum
        lst.append(resp)

        firstNum = secondNum
        secondNum = resp
    result = " ".join(str(x) for x in lst)
    return result


result = fibonacciSeq(10)
print(result)
