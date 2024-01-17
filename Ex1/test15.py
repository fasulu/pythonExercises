"""
Write a function called args2onent(args1, args2) that returns an int value 
of args1 raises to the power of args2.
Note here args2 is a non-negative integer, and the args1 is an integer.

args2ected output

Case 1:

args1 = 2
args2onent = 5

2 raises to the power of 5: 32 i.e. (2 *2 * 2 *2 *2 = 32)

Case 2:

args1 = 5
args2onent = 4

5 raises to the power of 4 is: 625 
i.e. (5 *5 * 5 *5 = 625)

"""
from operator import mul


def calcargs1args2onent(args1, args2):
    result = args1
    print(args1, args2)
    for x in range(1, args2):
        result = mul(args1, result)
    print(result)


calcargs1args2onent(5, 4)
