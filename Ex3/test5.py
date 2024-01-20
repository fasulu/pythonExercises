"""
Display numbers from a list using loop
Write a program to display only those numbers from a list 
that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to 
the next number. If the number is greater than 500, then stop the loop

Given: numbers = [12, 75, 150, 180, 145, 525, 50]

Expected output:

75
150
145

"""

lst = [12, 75, 150, 180, 145, 525, 50]


for num in lst:
    # print("Current Number",num)
    if num > 500:
        # print("Number is greater than 150")
        break
    elif num > 150:
        # print("Number is greater than 500")
        pass
    elif num < 151:
        # print("Number is less than 150")
        x = num % 5
        if x == 0:
            print(num)
        else:
            # print("Number is 150 and not divisible by 5")
            pass
