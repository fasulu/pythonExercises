"""
Remove first n characters from a string
Write a program to remove characters from a string starting from 
zero up to n and return a new string.

For example:

remove_chars("pynative", 4) so output must be tive. 
Here, we need to remove the first four characters from a string.
remove_chars("pynative", 2) so output must be native. 
Here, we need to remove the first two characters from a string.
Note: n must be less than the length of the string.

"""


def removeNletters(num, strings):
    print("Original string", strings)
    # print(strings[1:3])
    for x in range(num, len(strings)):
        print(strings[x])


removeNletters(3, "Programme")