"""
Exercise 6: Display numbers divisible by 5 from a list
Iterate the given list of numbers and print only those 
numbers which are divisible by 5

Expected Output:

Given list is  [10, 20, 33, 46, 55]
Divisible by 5
10
20
55

"""
import decimal


def divisibleByFive(li):
    print(li)
    for num in li:
        res = decimal.Decimal(int(num) / 5)
        res = round(res, 1)

        # converts res to string and split all numbers after decimal point
        result = str(res).split(".")[1]

        # any value of result is equal to 0
        if int(result) == 0:
            print(num)

    # Prof's method %5
    # for num in li:
    #     if num % 5 == 0:
    #         print(num)


divisibleByFive([10, 20, 33, 46, 55])
