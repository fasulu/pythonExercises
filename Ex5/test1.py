"""
Create a string made of the first, middle and last character
Write a program to create a new string made of an input 
string’s first, middle, and last character.

Given:

str1 = "James"
Expected Output:

Jms

"""
str1 = "James"
# str1 = "Banana"

length_ = round(len(str1)) // 2

print(str1[0])  # first

if len(str1) % 2:
    print((str1[length_]))  # middle
else:
    print((str1[length_ - 1]), (str1[length_]))  # middle

print(str1[len(str1) - 1])  # last
