"""
Use a loop to display elements from a given list present at odd 
index positions.

Given:
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

Expected output: 20 40 60 80 100

"""

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
resp = []
for x in range(1, len(my_list), 2):
    resp.append(my_list[x])  # append the result
print(" ".join(str(ls) for ls in resp))  # show the result in one line string format
