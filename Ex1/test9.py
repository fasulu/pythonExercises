"""
Check Palindrome Number
Write a program to check if the given number is a palindrome number.

A palindrome number is a number that is the same after reverse. 
For example, 545, is the palindrome numbers

Expected Output:

original number 121
Yes. given number is palindrome number

original number 125
No. given number is not palindrome number

"""


def palindrome(num):
    # to work entering number as string
    if num.isdigit():
        lst = []
        for x in str(num):
            # print(x)
            lst.insert(0, x)
        strX = " ".join(lst)
        result = strX.replace(" ", "")
        if str(num) == str(result):
            print("Original number ", num)
            print("Yes. given number is palindrome number ", result)
        else:
            print("Original number ", num)
            print("No. given number is not palindrome number ", result)
    else:
        print("Please enter a whole numbers")

    # to work entering number through terminal

    # response = isinstance(num, str)
    # if response:
    #     lst = []
    #     for x in str(num):
    #         # print(x)
    #         lst.insert(0, x)
    #     strX = " ".join(lst)
    #     result = strX.replace(" ", "")
    #     if str(num) == str(result):
    #         print("Original number ", num)
    #         print("Yes. given number is palindrome number ", result)
    #     else:
    #         print("Original number ", num)
    #         print("No. given number is not palindrome number ", result)
    # else:
    #     print("Please enter a whole numbers")


# inString = input("Please enter a whole number: - ")
# palindrome(inString)

palindrome("151")

# ************

# Prof's method

# def palindrome(number):
#     print("original number", number)
#     original_num = number

#     # reverse the given number
#     reverse_num = 0
#     while number > 0:
#         reminder = number % 10
#         reverse_num = (reverse_num * 10) + reminder
#         number = number // 10

#     # check numbers
#     if original_num == reverse_num:
#         print("Given number palindrome")
#     else:
#         print("Given number is not palindrome")

# palindrome(121)
# palindrome(125)
