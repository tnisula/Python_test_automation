"""
Exceptions are errors
We should handle exceptions in our code
to make sure the code is working the way we want and is handling all the unwanted issues
Link to 3.5 built-in exceptions - https://docs.python.org/3/library/exceptions.html
"""

def exceptionHandling():
    try:
        """
        Change a, b, c to show exceptions
        """
        a = 10
        b = 20  # Test "any string"
        c = 10  # Test 0
        d = (a + b) / c
        print(d)
    except:
        print("In the except block")
        raise Exception("This is my exception.")
    # except ZeroDivisionError as err:
    #    print('Handling run-time error:', err)
    # except TypeError:
    #    print("Can't add string to integer")
    else:
        print("Because there was no exceptions, else is executed")
    finally:
        print("Finally, always executed!")

exceptionHandling()

def exercise():
    car = {"make": "bmw", "model": "550i", "year": "2016"}
    try:
        print(car["color"])
    except:
        print("Key not found exception")
        # raise Exception("This is my exception.")
    else:
        print("Because there was no exceptions, else is executed")
    finally:
        print("Try another key!")

exercise()