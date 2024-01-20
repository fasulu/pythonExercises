"""
Print the following pattern
Write a program to use for loop to print the following reverse 
number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1

"""
lst = []
cnt = 5
while cnt > 0:
    for x in range(cnt, 0, -1):  # reads in reverse order
        lst.append(x)
    # print(lst)
    xd = " ".join(str(ls) for ls in lst)  # saves as string after removing commas
    print(xd)
    lst = []  # before next iteration empty lst
    cnt = cnt - 1  # deduce 1 from cnt to go down to 1
