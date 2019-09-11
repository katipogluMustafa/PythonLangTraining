# Print All the Keywords
import keyword

print(keyword.kwlist)

### True, False
print(1 == 1)
if True:
    print("Condition evaluates to true")

# Yeap True is the same as 1
if True == 1:
    print("True is equal to 1")

# False is the same as 0
if False == 0:
    print("False is equal to 0")

# But sorry, 2 is not considered as True
if True == 2:
    print("True equal to 2")
else:
    print("True is not equal to 2")

# Returns 2
print( True + True)

# as Excepted return 0
print(False + False)

# Lets do something crazy
total = 0;
for i in range(1,10):
    total += True
print(total)














