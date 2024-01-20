"""
Check file is empty or not
Write a program to check if the given file is empty or not

"""

from os import path

fileLoc = "/home/fasulu/Documents/pythonExercises/Ex2/new_file.txt"


def checkFileEmpty():
    flag = path.isfile(fileLoc)
    if flag:
        openFile = open(fileLoc, "r")

        if openFile.readlines():
            print("File has data")
        else:
            print("File is not empty")
        openFile.close()
    else:
        print("File does not exist")


checkFileEmpty()
