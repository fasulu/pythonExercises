"""
 Write a program to print multiplication table of a given number

For example, num = 2 so the output should be

2
4
6
8
10
12
14
16
18
20

"""


def acceptANum():
    inNum = int(input("Please enter a number:- "))
    return inNum


def prepareTable(num):
    for x in range(1, 10 + 1):
        print(num * x)


num = acceptANum()
prepareTable(num)
