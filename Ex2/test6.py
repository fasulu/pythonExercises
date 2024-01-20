"""
Write all content of a given file into a new file by skipping 
line number 5.

Given test.txt file:

line1
line2
line3
line4
line5
line6
line7

Expected Output: new_file.txt

line1
line2
line3
line4
line6
line7
"""


def writeTextFile(data):
    flag = data.find("5")
    print(type(flag))
    if flag >= 0:
        print("Line 5, not writing in new_file.txt", data)
    else:
        # open file with 'a' append flag to write
        writeFile = open("/home/fasulu/Documents/pythonExercises/Ex2/new_file.txt", "a")
        writeFile.write(data)
        writeFile.close()


def readTexfFile():
    openFile = open("/home/fasulu/Documents/pythonExercises/Ex2/test.txt", "r")

    # for lines in openFile:
    for dataLine in openFile.readlines():
        writeTextFile(dataLine)
    openFile.close()


readTexfFile()
