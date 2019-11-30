"""
Object Oriented Programming
"""
s = "This is a string"

s.upper()
s.lower()

print(type('s'))
print(type([1, 2, 3]))

class MyCar(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        print("Make of the car: " + self.make)
        print("Model of the car: " + self.model)


c1 = MyCar('bmw', '550i')
c1.wheels = 3
c1.info()

c2 = MyCar('benz', 'E350')
c2.info()

print(c1.wheels)
print(MyCar.wheels)

"""
Base class
"""
class Car(object):

    def __init__(self):
        print("You just created the car instance")

    def drive(self):
        print("Car started...")

    def stop(self):
        print("Car stopped...")


"""
Inherited class
Overriding a method of base class
"""
class BMW(Car):
    def __init__(self):
        Car.__init__(self)
        print("You just created the BMW instance")

    def drive(self):
        super().drive()
        print("You are driving a BMW, just enjoy!")

    def headup_display(self):
        print("This is a unique feature")


"""
Create instances
"""
c = Car()
c.drive()
c.stop()

b = BMW()
b.headup_display()
b.drive()
b.stop()


"""
Base class
"""
class Fruit(object):

    def __init__(self):
        print("You just created the fruit instance")

    def nutrition(self):
        print("Nutrition of fruit is...")

    def fruit_shape(self):
        print("Fruit's shape is...")


"""
Inherited class
Overriding a method of base class
"""
class Banana(Fruit):
    def __init__(self):
        Fruit.__init__(self)
        print("You just created the Banana instance")

    def nutrition(self):
        super().nutrition()
        print("Banana's nutrition is... just enjoy!")

    def color(self):
        print("Bananas are yellow!")


"""
Create instances
"""
f = Fruit()
f.nutrition()
f.fruit_shape()

ba = Banana()
ba.nutrition()
ba.fruit_shape()
ba.color()

"""
Scope and namespaces example
"""
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)


class Dog:

    kind = 'canine'         # class variable shared by all instances
    # tricks = []
    # Mistaken use of a class variable

    def __init__(self, name):
        self.name = name    # instance variable unique to each instance
        self.tricks = []  # Correct use! creates a new empty list for each dog

    def add_trick(self, trick):
        self.tricks.append(trick)


d = Dog('Fido')
e = Dog('Buddy')
print(d.kind)               # shared by all dogs
print(e.kind)               # shared by all dogs
print(d.name)               # unique to d
print(e.name)               # unique to e
d.add_trick('roll over')
e.add_trick('play dead')
print(d.tricks)             # unexpectedly shared by all dogs, if tricks declared wrongly
print(e.tricks)


# How to create a Pascal like record or a C Struct
class Employee:
    pass

john = Employee()  # Create an empty employee record

# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

x = Complex(3.0, -4.5)
print(x.r, x.i)

class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('Timo Nisula')
print(iter(rev))
for char in rev:
    print(char)

def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]

for char in reverse('Timo Nisula'):
    print(char)
