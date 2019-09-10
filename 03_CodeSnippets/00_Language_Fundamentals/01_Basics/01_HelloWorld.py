# Basic Printing

print('Hello, world')
print(1 + 2)
print(7 * 6)
print("The End")

# Concatenating

print("Hello" "World")  # Interpreter implicitly concatenates
print("Hello" + "World")  # Explicitly concatenate strings

# Use Variables

greeting = "Hello"
name = "Mustafa"
print(greeting + " " + name)

# Escape Sequences

escape_sequences = "Same \nas other\tlanguagesthey have"
print(escape_sequences)

# Strings implicitly contain newlines and tabs

str = """This string
    will be \
4 lines long
    even though it doesn't have
any escape sequence
"""
print(str)

str2 = """" if you use
    triple quotes, then you need to work about escaping
    any character inside.But remember
    "you can escape new line characters" inside \
    like so"""
print(str2)

# Take input

name = input("Please enter your name ")
# print(greeting + " " + name)      # uncomment


