x = 5
if x == 5:
    print("x is equal to 5")
elif x == 6:
    print("x is equal to 6")
elif x == 7:
    print("x is equal to 7")
else:
    print("x is not equal to 5,6 or 7")

# We can generate a sequence of numbers using range() function.
print( list(range(10)) )            # [0,10)
print( tuple(range(2,10)))          # [2,10)
print( set(range(0,15,3)) )         # in  range [0,15) multiples of 3


# iterate using for loop
genre = ['pop', 'rock', 'jazz']
for i in range(len(genre)):
    print("i don't like ", genre[i])

# for loop with else

# The else part is executed if the items in the sequence used in for loop exhausts.
# break statement can be used to stop a for loop. In such case, the else part is ignored.

def printArray(arr):
    for i in arr:
        print(i)
    else:
        print("No items left")

digits = [1,3,5,7,9,11,13,15]
empty_digits = []

printArray(digits)                      # executes for loop and else
printArray(empty_digits)                # executes else

# while loop with else

def count_odd_number(arr):
    count = 0
    i = 0
    if len(arr) == 0:
        return
    else:
        while i < len(digits):
            if arr[i] % 2 != 0:
                count += 1
                i += 1
        else:
            print("Out of loop")

    return count

print(count_odd_number(digits))         # executes while loop and else

# if code never reaches inside of loop, then no else will be execute

# pass keyword

for i in digits:
    pass                # nothing happens when pass is executed. It results into no operation (NOP)

def function(args):
    pass                # pass statement is not ignored like comments but results in no operation(NOP)

class Example:
    pass                # pass statements are used as placeholder, indicates it will be handled later