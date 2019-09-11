# Variables

# Basic Variable Assignment
x = 5

# init multiple variables
a, b, c = 5, 3.6, "Hello"

# assign the same value to multiple variables
x = y = z = "same value"

# Literals

a = 0b01100001      # binary literal
print(a)

b = 0o310           # Octal literal
print(b)

c = 0xffff          # hex literal
print(c)

f = 1.5e2           # exponential float literal
print(f)

d = 3.14j           # complex literal
print(d)

# Literal Collections

characters = ["x", "y", "z", "t"]           # list

numbers = (1,2,3,4)                         # Tuple

tr_dictionary = { "Hello": "Merhaba",
                  "Python": "Piton"}        # Dictionary

vowels = {'a', 'e', 'i', 'o', 'u'}          # Set

print(characters)
print(numbers)
print(tr_dictionary)
print(vowels)

