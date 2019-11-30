if 100 > 10:
    print("Number is greater than 10!")

value = 'yellow'
if value == 'green':
    print('Go!')
elif value == 'yellow':
    print('Prepare to stop!')
else:
    print('Stop!')

"""
Execure statemenst repeatedly
Condittions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
x = 0
while x < 10:
    print('Value of x is ' + str(x))
    x = x + 1

l = []
num = 0
while num < 10:
    l.append(num)
    num += 1

print(l)

"""
Break: To break out of the closest enclosing loop
Continue: Go to the start of the closest enclosing loop
"""

x = 0
while x < 10:
    print('Value of x is ' + str(x))
    x = x + 1
    if x == 5:
        break
    print('Testing break...')
    print('*'*20)
else:
    print('Just broke out of the loop 1')

print('-------------------------------')

x = 0
while x < 10:
    print('Value of x is ' + str(x))
    x = x + 1
    if x == 5:
        continue
    print('Testing continue...')
    print('*' * 20)
else:
    print('Just broke out of the loop 2')