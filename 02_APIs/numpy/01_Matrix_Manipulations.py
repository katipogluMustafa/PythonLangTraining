import numpy as np

def printDetails(array):
    print('\n',array)
    print("Shape: ", array.shape)
    print("Dimension: ", array.ndim)
    print("Data Type: ", array.dtype.name)
    print("Size: ", array.size)
    print("Type: ", type(array))

# Create 1* 8 Matrix
array = np.array([1,2,3,4,5,6,7,8])
printDetails(array)

# Convert 1*8 Matrix into 2*4 Matrix
array2 = array.reshape(2,4)
printDetails(array2)

# Directly Create 3*4 Matrix
array3 = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
printDetails(array3)

# Create Empty Matrix
zeroMatrix = np.zeros((2, 6))
print(zeroMatrix, '\n')

# Assign first row 6th column element to 5
zeroMatrix[0, 5] = 5
print(zeroMatrix, '\n')

# Create Matrix with all elements 1
allOnes = np.ones((3,2))
print(allOnes)

# Create Empty Matrix
emptyMatrix = np.empty((2,4))
print(emptyMatrix, '\n')

# like range function
    # create matrix with elements between 10 and 50 by incrementing 5 at a time
matrix = np.arange(10,50,5)
print(matrix)       # [10 15 20 25 30 35 40 45]

# interpolates 20 numbers with equal distances between 10 and 50
matrix2 = np.linspace(10,50,20)
print(matrix2)
