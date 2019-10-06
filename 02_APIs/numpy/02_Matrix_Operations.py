import numpy as np

# One Dimensional

a = np.array([1,2,3])
b = np.array([4,5,6])
print("a : ",a)
print("b : ",b)

print("a+b : ", a + b)
print("a-b : ", a - b)              # add or subtract corresponding elements in a and b

print("a*b: ",a*b)                  # Multiply corresponding elements

print("a**2 : ", a ** 2)
print("b**2 : ", b ** 2)            # takes square of each element in the matrix

print("sin(a) : ", np.sin(a))       # takes sin of each element in the matrix
print("sin(b) : ", np.sin(b))

print(a<2)  #[ True False False]    # prints whether condition true for each element as matrix

# Many Dimensional
print("\n")
a = np.array([[1,2,3,4]   , [5,6,7,8]])
b = np.array([[9,10,11,12], [13,14,15,16]])

print("a : ",a)
print("b : ",b)

print("a*b",a*b)                    # Elementwise multiplication

b = b.T                             # Take transpose
print("Transpoze of b: ",b)

print("a and b dot product: ", a.dot(b))                            # dot product

print("a.exp(): ", np.exp(a))       # take e to the power of each element in the matrix

a = np.random.random((5,5))         # Create 5*5 random matrix each element between 0 and 1
print(a)

print(a.sum())                      # sum all the elements
print(a.max())                      # maximum value in the matrix
print(a.min())                      # minimum value in the matrix

print(a.sum(axis=0))                # sum only elements inside 0th axis(columns)
print(a.sum(axis=1))                # sum only elements inside 1th axis(rows)

print(np.square(a))                 # Take square of each element
print(np.sqrt(a))                   # Take square root of each element
