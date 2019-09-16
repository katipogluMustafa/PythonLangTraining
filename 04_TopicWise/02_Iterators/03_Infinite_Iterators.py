# Infinite Iterators

# It is not necessary that the item in an iterator object has to exhaust.

# The built-in function iter() can be called with two arguments
# where the first argument must be a callable object (function) and second is the sentinel.
# The iterator calls this function until the returned value is equal to the sentinel.

print( int() )          # int() always returns 0

# int() never returns 1, never iterator stops
infinite_iterator_using_iter = iter(int, 1)     # until int() func returns 1, the iterator will iterate

print( next(infinite_iterator_using_iter) )
print( next(infinite_iterator_using_iter) )
print( next(infinite_iterator_using_iter) )


# Building Infinite Iterators

class InfIter:
    """Infinite iterator that returns squares of numbers"""

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        n = self.current ** 2
        self.current += 1
        return n
    
# Be careful to include a terminating condition, when iterating over these type of infinite iterators.
x = iter(InfIter())
print ( next(x) )
print ( next(x) )
print ( next(x) )
print ( next(x) )
print ( next(x) )

