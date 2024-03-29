"""
Append new string in the middle of a given string
Given two strings, s1 and s2. Write a program to create 
a new string s3 by appending s2 in the middle of s1.

Given:
s1 = "Ault"
s2 = "Kelly"

Expected Output:

AuKellylt

"""

s1 = "Ault"
s2 = "Kelly"

#method 1
s3 = s1[slice(0, 2)]
s3 = s1[slice(0, 2)] + s2 + s1[slice(2, 4)]
print(s3)

# method 2
middle=int(len(s1)/2)
s3 = s1[:middle:] + s2 + s1[middle:]
print(s3)
