"""
Tuples are like lists.
Tuples are immutable, but you can change lists
"""

my_list = [1,2,3]
print(my_list)
my_list[0] = 0
print(my_list)

my_tuple = (1,2,3,4,5,6)
print(my_tuple)
# my_tuple[0] = 0 Assignment not allowed

print(my_tuple[0])
print(my_tuple[1:])
print(my_tuple.index(4))
print(my_tuple.count(3))

t = 12345, 54321, 'hello!'
print(t)
u = t, (1, 2, 3, 4, 5)
print(u)

# tyhjä tuple ja 1 item tuplessa
empty = ()
single_item = 'hello',    # <-- note trailing comma
print(len(empty))
print(len(single_item))
print(single_item)
