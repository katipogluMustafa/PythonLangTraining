# Iterators

# Iterator in Python is simply an object that can be iterated upon.
# An object which will return data, one element at a time.

# Python iterator object must implement two special methods,
# __iter__() and __next__(), collectively called the iterator protocol.

# An object is called iterable if we can get an iterator from it.

odd_list = [1,3,5,7,9]

odd_iterator = iter(odd_list)       # get an iterator

print(next(odd_iterator))           # iterate through it using next()
print(next(odd_iterator))           # prints 3

## next(obj) is same as obj.__next__()
print(odd_iterator.__next__())
print(odd_iterator.__next__())
print(odd_iterator.__next__())
#print(odd_iterator.__next__())      # This will raise StopIteration error, no element left over

# We can use for loop
for i in odd_list:
    print(i)                        # uses iterator

# Here is How For Each loop implemented in Python
iter_object = iter(odd_list)        # odd_list is the iterable
while True:
    try:
        element = next(iter_object)
        # do something with it
    except StopIteration:
        # break the for loop
        break




