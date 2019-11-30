cars = ["bmw", "honda", "audi"]
empty_list = []

print(cars)
print(empty_list)

print('#'*20)
print(cars[1])

num_list = [1, 2, 3]
sum_num = num_list[0] + num_list[1]
print(sum_num)

more_cars = ["bmw", "honda", "audi"]
more_cars[1] = "Benz"
print(more_cars)

length = len(cars)
print(length)
cars.append("Benz")
print(cars)
cars.insert(1, "Jeep")
print(cars)

x = cars.index("honda")
print(x)

y = cars.pop()
print(y)
print(cars)
cars.remove("Jeep")
print(cars)

slicing = cars[0:2]
a = cars[1:]
print(slicing)
print(a)
cars.sort()
print(cars)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
print(fruits.index('banana'))
print(fruits.index('banana', 4))  # Find next banana starting a position 4
fruits.reverse()
print(fruits)
fruits.append('grape')
print(fruits)
fruits.sort()
print(fruits)
print(fruits.pop())

basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
for f in sorted(set(basket)):
    print(f)

squares = list(map(lambda x: x**2, range(10)))
print(squares)
cubes = [x**3 for x in range(10)]
print(cubes)

for i in reversed(range(1, 10, 2)):
    print(i)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    ]

print(list(zip(*matrix)))  # prefer zip
print([[row[i] for row in matrix] for i in range(4)])

transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print(transposed)

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))