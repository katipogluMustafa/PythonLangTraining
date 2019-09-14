# Classes

class MyNewClass:
    """This is a docstring."""
    pass

# MyClass.func is a function object (attribute of class), ob.func will be a method object.
class MyClass:
    """This is my second class docstring"""
    a = 10
    def func(self):
        print("Hello")

obj = MyClass()
print(MyClass.func)                 # <function MyClass.func at 0x013BD618>
print(obj.func)                     # <bound method MyClass.func of <__main__.MyClass object at 0x0130EE90>>
obj.func()                          # ob.func() translates into MyClass.func(ob).

    # Class functions that begins with double underscore (__) are called special functions as they have special meaning.
class ComplexNumber:
    def __init__(self, r = 0, i= 0):
        self.real = r
        self.imag = i

    def get_data(self):
        print("{0}+{1}j".format(self.real, self.imag))

c1 = ComplexNumber(5, 7)
c1.get_data()

c2 = ComplexNumber(10)
c2.attr = 10                # create a new attribute 'attr'
print( (c2.real, c2.imag, c2.attr) )

# But c1 object doesn't have attribute 'attr'
#print( (c1.real, c1.imag, c1.attr) )       # error, object has no attribute 'attr'


# Deleting Attributes and Objects
c1 = ComplexNumber(11, 3)
del c1.imag
#print( c1.imag )                           # error, object has no attribute 'imag'

del ComplexNumber.get_data
#c1.get_data()                              # error, object has no attribute 'get_data'

del c1                                      # delete object itself