# Data Types

# Everything is an object in python

# Numbers

# integers can be any length, limited by available memory
my_int = 454545454545445454545445545454454545454545454545454545445454545
print(my_int)

a = 5
print(a, "is a type of ", type(a) )

# A floating point number is accurate up to 15 decimal places
b = 5.0
print(b, "is a type of ", type(b) )

c = 5j
print(c, "is a type of ", type(c) )

if isinstance(a, int):
    print("Yeap a has a type of int")

## List

# List is an ordered sequence of items.

a = [1, 5.5, 'debug']

print("a[0] = ", a[0])
print("a[1] = ", a[1])
print("a[2] = ", a[2])

print("a[0:3] = ", a[0:3])
print("a[:3] = ", a[:3])
print("a[1:] = ", a[1:])

a[2] = "new string"         # Lists are mutable
print("a[:] = ", a[:])

# a[3] = "asd"              # out of range
print("a[:] = ", a[:])


## Tuple

# Tuple is an ordered sequence of items same as list.

t = (1, 5.5, 'debug')

#t[1] = 6.5      # Tuples are immutable, cant change values of its members
print("t[1] = ", t[1])
print("t[:] = ", t[:])
print("t[:3] = ", t[:3])
print("t[0:3] = ", t[0:3])
print("t[1:] = ", t[1:])

## Strings

# String is sequence of Unicode characters.
s = 'Hello World'

#s[4] = 'b'              # Strings are immutable
print("s[4] = ", s[4])

print("s[:] = ", s[:])
print("s[3:] = ", s[3:])
print("s[:5] = ", s[:5])
print("s[3:8] = ", s[3:8])


## Set

# Set is an unordered collection of unique items.
# Since, set are unordered collection, indexing has no meaning. Hence the slicing operator [] does not work.

my_set =  { 3, 5, 7, 9, 11}

print("my_set = ", my_set)

duplicates_will_be_eliminated = { 1, 1, 1, 2, 2, 2}
print(duplicates_will_be_eliminated)


## Dictionary

# Dictionary is an unordered collection of key-value pairs.

d = { 1 : "value", "key" : 2}
print(type(d))      # dict

print("d[1] = ", d[1] )         # key is 1
print("d['key'] = ", d['key'])  # key is key

# We use key to retrieve the respective value. But not the other way around.

## Conversion Between Data Types

print( float(5) )

print( int(5.6) )

# Conversion to and from string must contain compatible values.
print( float('2.5'), type(float('2.5')) )
print( str(25), type(str(25)) )

print( set([1,2,3]) )
print( list({1,2,3}) )
print( list('hello') )
print( tuple([1,3,5,7]) )

# To convert to dictionary, each element must be a pair

print( dict([[1,2],[3,4]]))
print( dict(((1,2),(3,4))))

