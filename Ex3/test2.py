"""
Print the following pattern
Write a program to print the following number pattern using 
a loop.

1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5

"""
x = 1
strX = ""
while x <= 6:
    for y in range(1, x):
        strX = strX + " " + str(y)
    print(strX)
    strX = ""
    x += 1
