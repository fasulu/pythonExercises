"""
1B: Create a string made of the middle three characters
Write a program to create a new string made of the 
middle three characters of an input string.

Given:

Case 1

str1 = "JhonDipPeta"
Output

Dip

"""
# str1 = "JhonDipPeta"
str1 = "JaSonAy"

length_ = round(len(str1)) // 2

print(len(str1), length_)
if length_ % 2:
    print(str1[slice(length_-1, length_+2)])

