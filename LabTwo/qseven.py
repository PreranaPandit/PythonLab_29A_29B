'''
7. Given a positive real number, print its fractional part.
'''

import math

a=float(input("enter the number: "))

'''
math.modf(x)
Return the fractional and integer parts of x. Both results carry the sign of x and are floats.

https://note.nkmk.me/en/python-math-modf/
'''
x,y=math.modf(a)
print(x)
print(y)

