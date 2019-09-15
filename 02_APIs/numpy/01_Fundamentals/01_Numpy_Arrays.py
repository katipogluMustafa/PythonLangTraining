# Numpy Arrays

# Create 2 new lists height and weight
height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

# Import the numpy package
import numpy

np_height = numpy.array(height)
np_weight = numpy.array(height)

print( type(np_height) )                # <class 'numpy.ndarray'>

# Element-wise calculation
bmi = np_weight / np_height ** 2
print(bmi)

# Subsetting
print(bmi > 23)             # for boolean response
print(bmi[bmi < 23])        #np_height print only those observations less than 23


# Practice
weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]
np_weight_kg = numpy.array(weight_kg)
np_weight_lbs = np_weight_kg / 2.2
print(np_weight_lbs)