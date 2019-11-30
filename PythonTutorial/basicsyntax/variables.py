"""
table
object reference count
"""

import keyword
print(keyword.kwlist)

a = "nyc"
b = "nyc"

print(a)

a = 123

print(a)
print(b)

b=456

print(b)

c='nyc'
d=c

print(c==d)
print(d is c)

a = b = c = 10
print(a)
print(b)
print(c)

x, y, z = 10, 20, 30
print(x)
print(y)
print(z)

