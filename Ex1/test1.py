"""
  Calculate the multiplication and sum of two numbers
  Given two integer numbers, return their product only 
  if the product is equal to or lower than 1000. Otherwise, 
  return their sum.
  
  Given 1: number1=20, number2=30, expected output 600
  Given 2: number1=40, number2=30, expected output 70
  
"""
from operator import mul, add


def calculate(num1, num2):
    res = mul(num1, num2)
    if res <= 1000:
        return res
    else:
        return add(num1, num2)


# Case 1
response = calculate(20, 30)
print("The result is", response)

# Case 2
response = calculate(40, 30)
print("The result is", response)
