def calc_tax(state_name, gross_income):

    state_dict = {'CA': 10, 'NY': 15, 'TX': 20, 'NJ': 22}
    net_income = gross_income - (gross_income * 10/100)
    if state_name in state_dict:
        net_income = net_income - (gross_income  * state_dict[state_name] / 100)
        print("Net income is " + str(net_income))
        return net_income
    else:
        print("State not in the list")
        return None

def fib(n):
    """Print a Fibonacci series up to n."""
    print("Printing fibonaccis less than", n)
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib_to_list(n):
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'Y', 'yes', 'YES'):
            return True
        if ok in ('n', 'N', 'no', 'NO'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

i = 5

def f(arg=i):
    print(arg)

i = 6
f()    # Notice! This will print 5

def fun1(a, L=[]):
    L.append(a)
    return L

def fun2(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

# Lambda expressions
def make_incrementor(n):
    return lambda x: x + n

fun3 = make_incrementor(42)
print(fun3(0))
print(fun3(1))

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
print(pairs)

print(fun1(1))
print(fun1(2))
print(fun1(3))

print(fun2(1))
print(fun2(2))
print(fun2(3))

fib(2000)
f100 = fib_to_list(100)
print(f100)
print()
ask_ok('Do you really want to quit? Y(es) / n(o) ? ')
ask_ok('OK to overwrite the file? Y / n ', 2)
ask_ok('Are you sure? y / N ', 2, 'Come on, only yes or no! ')
print()
test1 = calc_tax('CA', 21500)
test2 = calc_tax('NY', 23500)
test3 = calc_tax('TX', 27000)
test4 = calc_tax('MO', 23000)
print()
parrot(1000)  # 1 positional argument
parrot(voltage=1000)  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')  # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)  # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')  # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword