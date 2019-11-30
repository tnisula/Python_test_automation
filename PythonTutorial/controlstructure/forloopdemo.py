"""
Execure statemenst repeatedly
Conditions are used to stop the execution of loops
Iterable items are Strings, List, Tuple, Dictionary
"""
my_string = 'abcabc'
for c in my_string:
    if c == 'a':
        print('A', end=' ')
    else:
        print(c, end=' ')

print()

cars = ['bmw', 'benz', 'honda']
for car in cars:
    print(car)

nums = [1, 2, 3]
for num in nums:
    print(num * 10)

print('*' * 20)
d = {'one': 1, 'two': 2, 'three': 3}
for key in d:
    print(key + " " + str(d[key]))
for k, v in d.items():
    print(k + ' ' + str(v))

"""
Iterating multiple lists at the same time
"""
l1 = [1, 2, 3]
l2 = [6, 7, 8, 20, 30, 40]
for a, b in zip(l1, l2):
    print(a)
    print(b)

"""
Creates a sequence of numbers but does not save them to memory
Very useful to generate numbers
"""
print(list(range(0, 10)))

a = range(10, 20)
print(a)
print(type(a))
print(list(a))

b = range(10, 20, 2)
print(b)
print(type(b))
print(list(b))

for num in range(1, 4):
    print(num)