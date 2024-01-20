"""
Read line number 4 from the following file

Create a test.txt file and add the below content to it.

test.txt file:

line1
line2
line3
line4
line5
line6
line7

"""

from os import path

filename = "/home/fasulu/Documents/pythonExercises/Ex2/test.txt"


def readLine4(filename):
    lineCnt = 1
    flag = path.isfile(filename)

    if flag:
        openFile = open(filename, "r")
        for data in openFile:
            if lineCnt == 4:
                print(data)
            lineCnt = lineCnt + 1

        openFile.close()

        # or using <with>
        # with open(filename, "r") as openedFile:
        #   lineFound = openedFile.readlines()
        #   print(lineFound[4-1])
        # this code will open and closes automatically after its job.

    else:
        print("File not exist")


readLine4(filename)
