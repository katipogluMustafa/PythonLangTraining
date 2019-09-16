# Set Operations

A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

# Union
union = A | B
print(union)

union2 = A.union(B)
print(union2)

# Intersection

intersection = A & B
intersection2 = A.intersection(B)

print(intersection)
print(intersection2)

# Difference

difference = A - B
difference2 = A.difference(B)           # Returns the difference of two or more sets as a new set

print(difference)
print(difference2)

# Symmetric Difference
    # Symmetric Difference of A and B is a set of elements in both A and B except those that are common in both.

symmetric_diff = A ^ B
symmetric_diff2 = A.symmetric_difference(B)

print(symmetric_diff)
print(symmetric_diff2)

# Updates the set itself, all operations has _update versions like intersection_update

A.difference_update(B)
print(A)                    # Removes all elements of another set from this set

# Checks

print( A.isdisjoint(B) )    # Returns True if two sets have a null intersection
print( A.issubset(B) )      # Returns True if another set contains this set
print( A.issuperset(B) )    # Returns True if this set contains another set