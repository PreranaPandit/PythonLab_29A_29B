'''
8. Given a three-digit number. Find the sum of its digits.
'''

'''
def getSum(n):
    sum = 0
    while (n != 0):
        sum = sum + int(n % 10)
        n = int(n / 10)

    return sum


# Driver code
n = 687
print(getSum(n))
'''





'''
# The random() function generates
# a random fractional number from 0 to 1
from random import random

# When the number is multiplied by 900,
# a random number is obtained from 0 to 899.(9).
# If you add 100 to it,
# you get a number from 100 to 999.(9).
n = random() * 900 + 100

# The fractional part is discarded, the number is displayed
n = int(n)
print(n)

# The first digit (the most significant) of the number
# is extracted by dividing it by 100
a = n // 100

# The last digit of the number is deleted by dividing by 10 whole.
# Then finding the remainder when dividing by 10 extracts the last digit,
# which in the original number was in the middle.
b = (n // 10) % 10

# The last digit (the lowest digit) of the number is extracted
# by finding the remainder by division by 10.
c = n % 10

# The sum of digits is calculated and displayed on the screen.
print(a + b + c)
'''

from random import random

n = random() * 900 + 100
n = int(n)
print(n)

# The number is converted to a string type
s = str(n)

# The first [0] character of the string is extracted,
# converted to an integer.
# Similarly, the second [1] and the third [2].
a = int(s[0])
b = int(s[1])
c = int(s[2])

print(a + b + c)

