"""
Accept any three string from one input() call
Write a program to take three names as input from 
a user in the single input() function call.

Expected Output

Enter three string Emma Jessa Kelly
Name1: Emma
Name2: Jessa
Name3: Kelly


"""


def takeThreeInput():
    listName = []
    inputStrings = input("Please enter 3 Strings:- ")
    listName = inputStrings.split()
    return listName


def displayNames(listName):
    for x in range(len(listName)):
        print("Name" + str(x) + ":", listName[x])


listName = takeThreeInput()
displayNames(listName)
