"""
Calculate the sum of all numbers from 1 to a given number
Write a program to accept a number from a user and calculate 
the sum of all numbers from 1 to a given number

For example, if the user entered 10 the output should 
be 55 (1+2+3+4+5+6+7+8+9+10)

Expected Output:

Enter number 10
Sum is:  55

"""
from datetime import datetime


def acceptANum():
    inNum = int(input("Please enter a number:- "))
    sTime = datetime.now()
    return inNum, sTime


# Using for loop
def sumAllNum(num):
    inNum = num[0]
    sTime = num[1]
    resp = 0
    print(inNum)
    for x in range(1, inNum + 1):
        resp = resp + x
    consumedTime = datetime.now() - sTime
    return "By for loop, total is", resp, consumedTime


# Using white loop
# def sumAllNum(num):
#     inNum = num[0]
#     sTime = num[1]
#     resp = 0
#     cnt = 1
#     while cnt <= inNum:
#         resp = resp + cnt
#         cnt += 1
#     consumedTime = datetime.now() - sTime
#     return "By while loop, total is", resp, consumedTime


num = acceptANum()
resp = sumAllNum(num)  # for loop result is faster than while loop
print(resp)

"""
Time consumed to process 123456789;
for loop => seconds=7, microseconds=37371
while loop => seconds=11, microseconds=679105
"""
