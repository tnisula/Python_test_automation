"""
Data type to store more than one value in one variable name, in terms of key value pairs
Dictionary items are in brackets [] in key:value pairs, separated with "," {'k1':'v1','k2':'v2'}
Not sequenced, no indexing => Mapping
"""

car = {'make': 'bmw', 'model': '550L', 'year': 2016}
print(car)

d = {}
model = car['model']
print(model)
print(d)
d['one'] = 1
d['two'] = 2

print(d)

sum_1 = d['two'] + 8
print(sum_1)
d['two'] = d['two'] + 8
print(d)

"""
Nested dictionary:
d = {'k1': {'nestk1': 'nestvalue1', 'nestk2': 'nestvalue2'}} 
d['k1']['nestk1']
"""
cars ={'bmw': {'model':'550L', 'year': 2016}, 'benz': {'model':'E350', 'year': 2015}}
bmw_year = cars['bmw']['year']
print(cars)
print(bmw_year)
print(cars['benz']['model'])

print(car.keys())
print(cars.keys())
print(car.values())
print(cars.values())
print(car.items())
print((cars.items()))

car_copy = car.copy()
print(car_copy)
# car.clear()
print(car.pop('model'))
print(car)

# Sets
print('*'*40)
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)   # show that duplicates have been removed
print('orange' in basket)  # fast membership testing
print('crabgrass' in basket)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
print(a)      # unique letters in a
print(a - b)  # letters in a but not in b
print(a | b)  # letters in a or b or both
print(a & b)  # letters in both a and b
print(a ^ b)  # letters in a or b but not both

# looping techniques
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)




