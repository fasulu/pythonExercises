"""
Write a program to display all prime numbers within a range
Note: A Prime Number is a number that cannot be made by multiplying other whole numbers. A prime number is a natural number greater than 1 that is not a product of two smaller natural numbers

Examples:

6 is not a prime mumber because it can be made by 2×3 = 6
37 is a prime number because no other whole numbers multiply together to make it.
Given:

# range
start = 25
end = 50
Expected output:

Prime numbers between 25 and 50 are:
29
31
37
41
43
47

"""


def findPrimeNum(start, end):
    # print(start, end)

    lessThanForty(start)
    
    # greaterThanForty()
        
    # if start < 40:
    #     lessThanForty(start)
    # elif start > 40:
    #     greaterThanForty()


def lessThanForty(num):
    # to calculate prime number less than forty
    # formula : 6(n)- 1 and 6(n)+1
    print("lessThanForty", type(num))
    for x in range(1, 8, 1):
        resp = (6 * x) - 1
        lastDigit = repr(resp)[
            -1
        ]  # This will find any number ends with 5 (if ends it is not prime number)
        if lastDigit != "5":
            print(resp)

        resp = (6 * x) + 1
        lastDigit = repr(resp)[
            -1
        ]  # This will find any number ends with 5 (if ends it is not prime number)
        if lastDigit != "5":
            print(resp)
        if resp >= end:
            break
        elif resp >40:
          greaterThanForty()


def greaterThanForty():
    # to calculate prime number greater than forty
    # formula: n^2 + n + 41
    # print("greaterThanForty", 9)

    for x in range(1, 50, 1):
     
        resp = (x **2) + x + 41
        lastDigit = repr(resp)[
            -1
        ]  # This will find any number ends with 5 (if ends it is not prime number)

        if resp > end:
            break

        if lastDigit != "5":
            print(resp)


start, end = 25, 50

findPrimeNum(start, end)
