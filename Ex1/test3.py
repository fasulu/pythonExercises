"""
Print characters from a string that are present at an even index number
Write a program to accept a string from the user and display characters 
that are present at an even index number.

For example, str = "javascript" so you should display 'a','a','c','i','t'.

Expected Output:

Orginal String is  javascript
Printing only even index chars
a
a
c
i
t

"""


def showAlternate(args):
    print("Original string is " + args)
    for x in range(0, len(args), 2):
        print(args[x])

    # prof's method using slicing
    # x = list(args)
    # for i in x[0::2]:
    #     print(i)


showAlternate("javascript")
