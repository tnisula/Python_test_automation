import os

os.getcwd()      # Return the current working directory
os.chdir('c:\pythonoulu')   # Change current working directory
os.system('mkdir today')

dir(os)   # returns a list of all module functions
# help(os)  # returns an extensive manual page created from the module's docstrings

"""
For daily file and directory management tasks, the shutil module provides a higher level 
interface that is easier to use:
"""
# import shutil
# shutil.copyfile('data.db', 'archive.db')
# shutil.move('/build/executables', 'installdir')

import glob # for making file lists from directory wildcard searches
print(glob.glob('*.py'))

import sys # process command line arguments
print(sys.argv)
# The most direct way to terminate a script is to use sys.exit().

import re # regular expressions
re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')

# Mathematics
import math
print("Cosine expression : " + str(math.cos(math.pi / 4)))
print("Logaritm expression : " + str(math.log(1024, 2)))

import random
print("Random choice : " + random.choice(['apple', 'pear', 'banana']))
print("Sample without replacement : " + str(random.sample(range(100), 10)))
print(random.random())        # random float
print(random.randrange(100))    # random integer chosen from range(100)

import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print("Mean of the data : " + str(statistics.mean(data)))
print("Median of the data : " + str(statistics.median(data)))
print("Variance of the data : " + str(statistics.variance(data)))

# dates are easily constructed and formatted
from datetime import date
now = date.today()
print("Today is : " + str(now))
print("Date formatting : " + now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))
# datetime.date(2003, 12, 2)
# '12-02-03. 02 Dec 2003 is a Tuesday on the 02 day of December.'

# Dates support calendar arithmetic
birthday = date(1962, 3, 13)
age = now - birthday
print("You have lived " + str(age.days) + " days.")

from timeit import Timer
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())

# Using doctest package to quality control
def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
print(doctest.testmod())   # automatically validate the embedded tests

import unittest
class TestStatisticalFunctions(unittest.TestCase):
	
    def test_average(self):
        self.assertEqual(average([20, 30, 70]), 40.0)
        self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
        with self.assertRaises(ZeroDivisionError):
            average([])
        with self.assertRaises(TypeError):
            average(20, 30, 70)
        print("Testing test_average function!")

unittest.main()  # Calling from the command line invokes all tests