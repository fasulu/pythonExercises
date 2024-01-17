"""
Return the count of a given substring from a string
Write a program to find how many times substring 
“Emma” appears in the given string.

Given:

str_x = "Emma is good developer and Emma is also a good writer"

Expected Output: Emma appeared 2 times

"""


def findEmma(str_x):
    lstWord = []
    lstWord = str_x.split()
    # print(lstWord)
    counter = 0
    for x in lstWord:
        if x.upper() == "EMMA":
            counter = counter + 1

    print("Emma appeared", str(counter), "times")


str_x = "Emma is good developer and Emma is also a good writer"
findEmma(str_x)

# ***********

# Prof's method 1
# str_x = "Emma is good developer. Emma is a writer"
# # use count method of a str class
# cnt = str_x.count("Emma")
# print(cnt)

# ***********

# Prof's method 2
# def count_emma(statement):
#     print("Given String: ", statement)
#     count = 0
#     for i in range(len(statement) - 1):
#         count += statement[i: i + 4] == 'Emma'
#     return count

# count = count_emma("Emma is good developer. Emma is a writer")
# print("Emma appeared ", count, "times")
