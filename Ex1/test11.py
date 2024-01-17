"""
Write a Program to extract each digit from an integer in the reverse order.
For example, If the given int is 7536, the output shall be “6 3 5 7“, 
with a space separating the digits.

"""


def reverseOrder(num):
    print(num)
    res = ""
    for x in str(num):
        res = x + " " + res
    print(res)


reverseOrder(7536)

# *********

# Prof's method

# number = 7536
# print("Given number", number)
# while number > 0:
#     # get the last digit
#     digit = number % 10
#     # remove the last digit and repeat the loop
#     number = number // 10
#     print(digit, end=" ")
