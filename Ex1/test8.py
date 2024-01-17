"""
Print the following pattern using for loop
1 
2 2 
3 3 3 
4 4 4 4 
5 5 5 5 5

"""


def pattern(num):
    # print(num)
    for x in range(0, num + 1):
        print(str(x) * x)


pattern(5)

# **********

# Prof's method

# for num in range(5):
#     for i in range(num):
#         print(num, end=" ")  # print number
#     # new line after each row to display pattern correctly
#     print("\n")
