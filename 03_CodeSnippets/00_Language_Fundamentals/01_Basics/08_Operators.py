
print("5/2 = ", 5/2)        # float division
print("5//2 = ", 5//2)      # int division

print("5**2 = ", 5**2)      # Exponent

# identity operators

### Checks whether they point to the same memory or not

x1 = [1,2,3]
y1 = [1,2,3]

print(x1 is y1)             # False
print( x1 is not y1)        # True


# Membership operator

### Test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary)

x = 'Hello world'
print( 'H' in x)            # True
print( 'z' in x )           # False

### we can only check keys of a dictionary
y = { 1:'a', 2:'b'}
print( 1 in y)              # True




