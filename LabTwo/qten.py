'''
10.  Write a Python program to sum of three given integers. However,
if two values are equal sum will be zero.
'''


def sum(a, b, c):
    if a == b or b == c or c == a:
        sum = 0;
    else:
        sum = (a + b + c)
    return sum


x, y, z = [int(a) for a in input("Enter Three Number: ").split(",")]

print(sum(x, y, z))