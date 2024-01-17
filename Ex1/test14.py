"""
Print a downward Half-Pyramid Pattern of Star (asterisk)
* * * * *  
* * * *  
* * *  
* *  
*

"""


def halfPramid(num):
    counter = num
    character = ""
    while counter > 0:
        for x in range(1, counter):
            character = character + "*"
        print(character)
        character = ""
        counter = counter - 1


halfPramid(6)

# ************

# Prof's method

# for i in range(6, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")
