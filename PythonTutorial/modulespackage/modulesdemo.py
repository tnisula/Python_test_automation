"""
https://docs/python.org/3/library
"""

import math
from math import sqrt

# import modulesexternal.car as car
# from modulesexternal import car   #  better way to do it

from modulesexternal.car import info
# from modulesexternal.fibo import *
from modulesexternal import fibo

class ModulesDemo():

    def builtin_modules(self):
        print(math.sqrt(100))
        print(sqrt(100))

    def car_description(self):
        make = "bmw"
        model = "550i"
       # car.info(make, model)
        info(make, model)

m = ModulesDemo()
m.builtin_modules()
m.car_description()

print(fibo.__name__)
print(fibo.fib(1000))
print(fibo.fib2(1000))

import sys
print(dir(fibo))
print(dir())

import builtins
print(dir(builtins))