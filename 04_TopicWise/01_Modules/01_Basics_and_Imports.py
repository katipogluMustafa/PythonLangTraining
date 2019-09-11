# Functions, modules and packages are all constructs in Python that promote code modularization.

## Module Search Path
import sys


def print_sys_path():
    print("\nPrinting each path That will be search for Module imports\n")
    for path in sys.path:
        print(path)


# Lets dynamically add a folder to sys.path
if 'C:\Dev\PySeries' in sys.path:
    print("'C:\Dev\PySeries' is found at sys.path...\n")
else:
    print("Appending the path to sys.path")
    sys.path.append('C:\Dev\PySeries')
    print_sys_path()

## The statement import <module_name> only places <module_name> in the caller’s symbol table.
# The objects that are defined in the module remain in the module’s private symbol table.
import math

print(math.cos(0))  # access that modules private symbols using module name
print(math.cos(89))

## An alternate form of the import statement allows individual objects from
# the module to be imported directly into the caller’s symbol table:
from math import cos, sin

print(cos(0))
print(cos(89))
print(sin(1))
print(sin(90))


## Because this form of import places the object names directly into the caller’s symbol table,
# any objects that already exist with the same name will be overwritten

def tan(x):
    return 1


from math import tan

print(tan(5))  # overrides the original tan

# import everything from a module at once

from math import *  # Quite dangerous import
# This will place the names of all objects from <module_name> into the local symbol table,
# with the exception of any that begin with the underscore (_) character.
print(atan(1))

## It is also possible to import individual objects but enter them into the local symbol table with alternate names

from math import cos as my_cos, sin as my_sin

print(my_cos(20))
print(my_sin(20))

## You can also import an entire module under an alternate name

import math as my_math

print(my_math.cos(20))

## Guard against unsuccessful import attempts

try:
    # Non-existent module
    import my_module
except ImportError:
    print("Module not found...")

## Module contents can be imported from within a function definition.
# In that case, the import does not occur until the function is called:

def my_func():
    from math import cosh          # in functinos you can use 'import *'
    print(cosh(5))

    

