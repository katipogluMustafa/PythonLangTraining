## Tuple

classic_tuple = (1, 3, 5, 7, 9)         # (1, 3, 5, 7, 9)
print(classic_tuple)                    # can not change items of a tuple

mixed_tuple = ( "Hello", 1, 2.0)
print(mixed_tuple)                      # ('Hello', 1, 2.0)

free_style_tuple = 3, 4, 5              # parenthesis are optional
print(free_style_tuple)                 # (3, 4, 5)

free_style_tuple2 = "Selam", 5,0, 1
print(free_style_tuple2)                # ('Selam', 5, 0, 1)

a, b, c = free_style_tuple              # tuple unpacking
print(a)                    # 3
print(b)                    # 4
print(c)                    # 5



# One Element Tuple

my_tuple = ("Hello",)                           # you must add trailing comma,
# otherwise it will be in this case string
print("Type of my_tuple is ", type(my_tuple))   # Type of my_tuple is  <class 'tuple'>

mystr = ("Another Hello")                       # no trailing comma, no tuple
print("Typeof mystr is ", type(mystr))          # Type of free_one  <class 'tuple'>

free_one = 1,
print(  "Type of free_one " , type(free_one) )  # Type of free_one  <class 'tuple'>



# Changing Tuple Elements

# Tuples are immutable.

# Elements of a tuple cannot be changed once it has been assigned
# But, if the element is itself a mutable datatype like list, its nested items can be changed.
ex_tuple = (1, 3, 5, [7, 9, 11])
ex_tuple[3][1] = 13
print(ex_tuple)                                 # (1, 3, 5, [7, 13, 11])

# Tupes can be reassigned
ex_tuple = ('a', 'b')
print(ex_tuple)



# Concatenation

ex_tuple = (1,3,5) + (2,4,6)
print( ex_tuple )                               # (1,3,5,2,4,6)



# Repeat
ex_tuple = (1,2) * 3                            # (1,2,1,2,1,2)
print(ex_tuple)


# Deletion

## Can't delete each element but we can delete tuple itself
del ex_tuple
#print(ex_tuple)                                # ex_tuple is not defined



# count(x)

ex_tuple = ('a')
ex_tuple *= 5
print( ex_tuple.count('a') )                    # 5



# index(x)

# Returns the index of the first item that is equal to x
ex_tuple = 'e', 'b', 'c', 'a', 'd', 'a'
print( ex_tuple.index('a') )                    # 3



 # Membership Test
  
 print( 'f' in ex_tuple )                      # False
 print( 'a' in ex_tuple )                      # True
 print( 'a' not in ex_tuple )                  # False



# Advantages of Tuple over List

## Since tuples are immutable, iterating through tuple is faster than with list.
## Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
## If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.
