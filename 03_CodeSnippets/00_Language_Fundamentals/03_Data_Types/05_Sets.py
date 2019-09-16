# Sets

    # A set is an unordered collection of items.
    # Every element is unique (no duplicates) and must be immutable (which cannot be changed).
    # However, the set itself is mutable. We can add or remove items from it.
    # A set cannot have a mutable element, like list, set or dictionary, as its element.

int_set = {1, 3, 5, 7, 9}
print(int_set)

mixed_set = {"Hello", 1.0, 2, (1,2,3)}
print(mixed_set)

my_set = set([1, 3, 5, 7])      # we can convert a list to a set
print(my_set)

# Empty curly braces creates empty dictionary not empty set
dict = {}
print(type(dict))

# use set() to init empty set

empty_set = set()
print(type(empty_set))

# Adding items:
    # Set dos not support indexing
    # use add() to add single element, update to add multiple elements
even_set = {2,4,6}
even_set.add(0)
print(even_set)

# The update() method can take tuples, lists, strings or other sets as its argument.
even_set.update([8, 10, 12])
print(even_set)

even_set.update((14,16), {18,20})
print(even_set)

# Removing items:
    # discard() if the item does not exist in the set, it remains unchanged.
    # remove() will raise an error
print("Before removal", even_set)
even_set.discard(12)
print(even_set)

even_set.discard(1)         # no action
print(even_set)

try:
    even_set.remove(15)
    print(even_set)
except KeyError:
    print("The {} does not exists...".format(15))

    # remove and return an random item using the pop() method
print(even_set.pop())
print(even_set)

    # clear all items in the set
even_set.clear()
if len(even_set) == 0:
    print("No item exists in the set...")
else:
    print(even_set)


