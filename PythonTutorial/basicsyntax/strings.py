"""
Examples how strings work in python

Sequence of characters
Contains a-z, 0-9, @
in double or single quotes
"""

a = "This is a simple string"
b = 'Using single quotes'

print(a)
print(b)

c = "Need to use 'quotes' inside a string"
print(c)

d = "Another way to handle \"quotes\""
print(d)

a = "This is a single string,\
 which is in two lines."
print(a)

# Examples to show some string functions
first = "New York City"[0]
city = "Helsinki"
print(first)
print(city[0])

stri = "This Is a Mixed Case"
print(stri.lower())
print(stri.upper())
print(len(stri))

"""
Concatenation
"""
print(stri + str(2))
print("Hello " + " " + " World !!!")

a = "1abc2abc3abc4abc"
print(a.replace("abc", "ABC"))
print(a.replace("abc", "ABC", 2))
"""
Sub strings
starting index is inclusive
ending index is exclusive
"""
sub = a[1:6]
step = a[1:6:2]
print(sub)
print(step)

a = "This is a string"
print(a[:])
print(a[1:])
print(a[:6])
print(a[-2])
print(a[:-1])
print(a[:len(a)])
print(a[::-1])

city = "Helsinki"
event = "Magic Show"

print("Welcome to " + city + " and enjoy the event " + event)
print("Welcome to %s and enjoy the event %s" %(city, event))

yes_votes = 42572654
no_votes = 43132495
percentage = yes_votes / (yes_votes + no_votes)
print('{:-9} YES votes  {:2.2%}'.format(yes_votes, percentage))

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}
for key, value in sorted(table.items(), key=lambda x: x[0]):
    print("{} : {}".format(key, value))
for key, value in sorted(table.items(), key=lambda x: x[1]):
    print("{} : {}".format(key, value))
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
