"""
Accept numbers from a user
Write a program to accept two numbers from the user and calculate 
multiplication


"""
from operator import mul


def multiply(args1, args2):
    result = mul(args1, args2)
    print(result)


str1 = int(input("Please enter 1st number:-"))
str2 = int(input("Please enter 2nd number:-"))
multiply(str1, str2)
