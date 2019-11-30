"""
Methods:
A group of code statements which can perform some specific task
Methods are reusable and can be called when needed in the code
"""
def sum_num(n1, n2):
    """
    Get sum of two numbers
    :param n1:
    :param n2:
    :return:
    """
    return(n1 + n2)

sum1 = sum_num(2, 5)
sum2 = sum_num(2, 4)

print(sum1)
print(sum2)

string_add = sum_num('one', 'two')
print(string_add)

l = [1, 2, 3, 4]
l.append(5)
print(l)
print(len(l))

print('*'*20)
def isMetro(city):
    l = ['sfo', 'nyc', 'la']
    if city in l:
        return True
    else:
        return False

x = isMetro('sfo')
print(x)
print(isMetro('Boston'))

print('*'*20)
"""
Positional Parameters
They are like optional parameters
and can be assigned a default value, if no value is provided from outside
"""
def sum_numbers(n1, n2 = 4):
    return n1 + n2

sum3 = sum_numbers(3)
print(sum3)
sum3 = sum_numbers(3, n2=12)
print(sum3)

"""
Variable Scope
"""
print('*'*20)
a = 10

def test_method(a):
    print("Value of local 'a' is " + str(a))
    a = 2
    print("New value of local 'a' is " + str(a))

def test_method2():
    global a
    print("Value of 'a' inside test method2 is " + str(a))
    a = 2
    print("New value of 'a' changed to " + str(a))

print("Value of global a is " + str(a))
test_method(a)
print("Did value of global a change? " + str(a))
test_method2()
print("Did value of global a change? " + str(a))

"""
Built-in functions
"""
print('*'*20)
def largest_num(*args):
    print(max(args))
    return(max(args))

def smallest_num(*args):
    print(min(args))

def abs_function(a):
    print(abs(a))

largest_num(-20, -10, 0, 10, 100)
smallest_num(-20, -10, 0, 10, 100)
abs_function(-20)
abs_function(20)

print(type(99))
print(type(99.9))
print(type("99.9"))
l = [1, 2, 3]
print(type(l))

