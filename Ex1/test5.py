"""
Check if the first and last number of a list is the same
Write a function to return True if the first and last number 
of a given list is same. If numbers are different then return False.

Given:
numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]

Expected Output:

Given list: [10, 20, 30, 40, 10]
result is True

numbers_y = [75, 65, 35, 75, 30]
result is False

"""


def firstAndLastSame(*args):
    # print(listA[1], len(listB))

    for x in args:
        firstNum = x[1 - 1]
        lastNum = x[len(x) - 1]
        if firstNum == lastNum:
            print("Given list ", x, "\nresult is", True)
        else:
            print("Given list ", x, "\nresult is", False)


l1 = [10, 20, 30, 40, 10]
l2 = [75, 65, 35, 75, 35]
firstAndLastSame(l1, l2)
