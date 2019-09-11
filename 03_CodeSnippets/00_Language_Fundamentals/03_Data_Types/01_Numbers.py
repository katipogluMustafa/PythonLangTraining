number = 5
print("is number an int ? :", isinstance(number, int ) )
print("Type of 'number' is" , type(number))

print("Type of '5.7' is", type(5.7))
print("Type of '1 + 21j' is", type(1+2j))

# Type Conversion

print( type(int(2.3)) )             # int, value 2
# When converting from float to integer, the number gets truncated (integer that is closer to zero)
print( type(int(-2.8)) )            # int, value -2
print( type(float(2)) )             # float, value 2.0
print( type(complex('1+2j'))  )     # complex, value 1+2j


# Python Decimal

import decimal

print(0.1)                          # output 0.1

print(decimal.Decimal(0.1))         # 0.1000000000000000055511151231257827021181583404541015625

from decimal import Decimal as D

print(1.1 + 2.2)                    # 3.3000000000000003
print( D('1.1') + D('2.2') )        # 3.3

print(1.2 * 2.50)                   # 3.0
print( D('1.2') * D('2.50')  )      # 3.000


## We generally use Decimal in the following cases.
# When we are making financial applications that need exact decimal representation.
# When we want to control the level of precision required.
# When we want to implement the notion of significant decimal places.
# When we want the operations to be carried out like we did at school


# Python Fractions

import fractions

print( fractions.Fraction(5) )       # 5
print( fractions.Fraction(1,3) )     # 1 / 3
print( fractions.Fraction(1.5) )     # 3 / 2

# instead of first one use second one
# to not to get wrong results because of binary inaccuracy
print( fractions.Fraction(1.1))     # 2476979795053773 / 2251799813685248
print( fractions.Fraction('1.1'))   # 11 / 10

# This datatype supports all basic operations.
from fractions import Fraction as F

print(  1 / F(5,6) )                # 6 / 5
print(F(1, 3) + F(4, 3))            # 5 / 3


# Mathematics

import math

print( "pi =", math.pi )
print( "cos(pi) =", math.cos(math.pi) )
print( "exp(2) =", math.exp(2) )
print( "log10(100) =", math.log10(100) )
print( "sinh(0.5) =", math.sinh(0.5) )
print( "5! =", math.factorial(5) )

# Random

import random

print( random.randrange(10,20))

x = ['a', 'b', 'c', 'd', 'e']
print(random.choice(x))                 # get random choice

random.shuffle(x)
print(x)                                # print shuffled x
print( random.random() )                # print random element