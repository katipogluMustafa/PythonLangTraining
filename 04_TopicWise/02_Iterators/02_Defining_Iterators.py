# Building Iterators

# We have to implement the methods __iter__() and __next__().

# The __iter__() method returns the iterator object itself. If required, some initialization can be performed.
# The __next__() method must return the next item in the sequence. On reaching the end, and in subsequent calls, it must raise StopIteration.

class PowTwo:
    """Class to implement an iterator of powers of two"""

    def __init__(self, max = 0):
        self.max = max

    def __iter__(self):
        self.current = 0
        return self

    def __next__(self):
        if self.current <= self.max:
            result = 2 ** self.current
            self.current += 1
            return result
        else:
            raise StopIteration

x = PowTwo(5)
x_iter = iter(x)
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))
print(next(x_iter))

# lets use for loop to iterate on our class
for i in PowTwo(4):
    print(i)
