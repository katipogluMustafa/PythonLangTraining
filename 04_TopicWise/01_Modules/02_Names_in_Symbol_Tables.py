## The built-in function dir() returns a list of defined names in a namespace.
mylist = [1, 2, 3, 4, 5, 6]

print(dir())
for i in dir():
    if i == 'mylist':
        print("yeap mylist is found...")

class Animal:
    pass

x = Animal()
print(dir())

## This can be useful for identifying what exactly has been added to the namespace by an import statement

from math import *

print(dir())

## We can also see just the names in a module's symbol table
import sys
print(dir(sys))


