"""
Display float number with 2 decimal places using print()

Given: num = 458.541315

Expected Output: 458.54

"""

num = 458.548315
print(num)  # 458.548315
print("{:.2f}".format(num))  # 458.55
print("%.2f" % round(num, 2))  # 458.55
print(float("{:.2f}".format(num)))  # 458.55
print(round(num, 2))  # 458.55
