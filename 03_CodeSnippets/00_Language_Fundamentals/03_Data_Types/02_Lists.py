## Lists


# Python allows negative indexing for its sequences.
# The index of -1 refers to the last item, -2 to the second last item and so on.

odd_list = [1,3,5,7,9]
print( odd_list[-1] )        # 9
print( odd_list[-2] )        # 7
#print( odd_list[-6] )       # index out of range

print( odd_list[-5:-1] )     # [1, 3, 5, 7]
print( odd_list[:-1]  )      # [1, 3, 5, 7]
print( odd_list[1:]  )       # [3, 5, 7, 9]

odd_list[1:4] = [11, 13, 15]
print( odd_list[:] )         # [1, 11, 13, 15, 9]

odd_list[0] = 17
print( odd_list[:] )         # [17, 11, 13, 15, 9]



# Add item

odd_list.append(21)
print( odd_list[:] )         # [17, 11, 13, 15, 9, 21]

odd_list.extend( [23, 25, 27, 29] )
print( odd_list[:] )         # [17, 11, 13, 15, 9, 21, 23, 25, 27, 29]



# Concatenation

new_odd = odd_list + [1, 3, 5]
print(new_odd[:])            # [17, 11, 13, 15, 9, 21, 23, 25, 27, 29, 1, 3, 5]

# Repeat for a given number of times

repeated_even = [2,4]
repeated_even *= 3
print(repeated_even)         # [2, 4, 2, 4, 2, 4]

# Inserting an item at specific index
odd = [1, 3]
odd.insert(0,-1)
print(odd)                   # [-1, 1, 3]

# Inserting multiple items at specific index

even = [6, 12]
even[1:1] = [8, 10]          # insert multiple elements at index 1
print(even)                  # [6, 8, 10, 12]

even[0:0] = [0,2,4]         # insert multiple elements at index 0
print(even)                 # [0, 2, 4, 6, 8, 10, 12]




# Deleting Elements

print(even)                 # [0, 2, 4, 6, 8, 10, 12]
del even[0]
print(even)                 # [2, 4, 6, 8, 10, 12]

del even[2:4]
print(even)                 # [2, 4, 10, 12]

del even                    # delete whole list
#print(even)                 # NameError: name 'even' is not defined

char_list = ['m', 'e', 'r', 'h','a','b','a']
print(char_list)            # ['m', 'e', 'r', 'h', 'a', 'b', 'a']

char_list.remove('r')       # remove 'r'
print(char_list)            # ['m', 'e', 'h', 'a', 'b', 'a']

char_list.pop()             # remove last item
print(char_list)            # ['m', 'e', 'h', 'a', 'b']

char_list.pop(0)            # remove index 0
print(char_list)            # ['e', 'h', 'a', 'b']

char_list.clear()
print(char_list)            # []

int_list = [1, 2, 3, 4, 5]
print(int_list)             # [1, 2, 3, 4, 5]

int_list[1:3] = []
print(int_list)             # [1, 4, 5]

int_list = []
print(int_list)             # [] -> surprise :P

numbers = [1, -2, 3, -4, 5, -6, 7, -8]
numbers.sort()
print(numbers)              # [-8, -6, -4, -2, 1, 3, 5, 7]

numbers.reverse()
print(numbers)              # [7, 5, 3, 1, -2, -4, -6, -8]



# Creating New List

power_of_three = [ 3 ** x for x in range(5) ]
print(power_of_three)      # [1, 3, 9, 27, 81]

pow2 = []
for x in range(10):         # code is same as upper list creation
   pow2.append(2 ** x)
print(pow2)

pow4 = [ 4 ** x for x in range(10) if x > 3]
print(pow4)                 # [256, 1024, 4096, 16384, 65536, 262144]

even = [ x for x in range(25) if x % 2 == 0]
print(even)                 # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24]

print( [ x+y for x in ['C++ ', 'C '] for y in['Language', 'Programming']] )
# ['C++ Language', 'C++ Programming', 'C Language', 'C Programming']



# List Membership Test

char_list = [ 's', 'e', 'l', 'a', 'm']
print( 'e' in char_list )           # True
print( 'k' not in char_list )       # True