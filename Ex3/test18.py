"""
Print the following pattern
Write a program to print the following start pattern using the for loop

* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*

"""


def pattern(num):
    print()
    star = "*"
    for x in range(num + 1):
        print(star * int(x))
    for y in range(-(num - 1), -0):
        print(star * int(str(-y)))


pattern(5)
