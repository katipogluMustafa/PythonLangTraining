# Strings

# Creating Strings
my_str = 'Hello';               # Method 1
print(my_str)

my_str1 = "Hello";              # Method 2
print(my_str1)

my_str2 = '''Hello''';          # Method 3
print(my_str2)

# Multiline Strings using Triple Quotes
my_multiline_str = """Hello...
                    This is a multiline String"""
print(my_multiline_str)

my_multiline_str2 = '''Hello...
                    Here is another multiline String'''
print(my_multiline_str2)

# Indexing
my_str = "Mustafa Katipoglu"
print("my_str = ", my_str)

print("my_str[0] = ", my_str[0]);       # First Character
print("my_str[-1] = ", my_str[-1]);     # Last Character
print("my_str[1:5] = ", my_str[1:5]);   # Slicing 2nd to 5th char
print("my_str[5:-2] = ", my_str[5:-2]); # Slicing 6th to 2nd last character

#print(my_str[20])                       # Index Out of range

# Changing Strings
del my_str          # we can only delete string entirely or reassign
#Strings are immutable.

# Concatenation

str1 = "Hello, "
str2 = "Wrold!"
print( "str1 + str2", str1 + str2 )
print( "str1 * 3", str1 * 3 )
print("See the concationation" " in place by writing to strings together")

s = ("Hello "
            "World!")               # concatenate using parenthesis if they are on different lines
print(s)


# Iterating Through Strings
l_count = 0
for letter in "Hellloo World!...":
    if letter == 'l':
        l_count += 1
print(l_count, "letters found")

# Membership Test
print( 'a' in "Program")
print( 'b' not in 'Program')

# Built-in functions
my_str = "TCP-IP"
    # enumerate
list_enumerate = list(enumerate(my_str))
print("list(enumerate(my_str)) = ", list_enumerate)
    # Character Count
print("len(my_str) is", len(my_str))

# Ignoring Escape Sequences
    # place r or R in front of the string.
    # This will imply that it is a raw string and any escape sequence inside it will be ignored.
print("This is \x61 \ngood example")
print(r"This is \x61 \ngood example")
print(R"This is \x61 \ngood example")

# Formatting Strings using format()
    # default(implicit) order
default_order = "{}, {} and {}".format("Mustafa", "Ahmet", "Abdullah")
print("\n--- Default Order ---\n",default_order)

    # order using positional argument
positional_order = "{1}, {0} and {2}".format("Mustafa", "Ahmet", "Abdullah")
print("\n--- Positional Order ---\n", positional_order)

    # order using keyword argument
keyword_order = "{a}, {abdul} and {m}".format(m="Mustafa", a="Ahmet", abdul="Abdullah")
print("\n--- Keyword Order ---\n", keyword_order)

    # formatting integers
print("Binary representation of {0} is {0:b}".format(25))
    # formatting floats
print("Exponent representation: {0:e}".format(1453.304))
    # round
print("one third is: {0:.3f}".format(1/3))
    # string alignment
    # left-justify <, right-justify > or center ^ a string in the given space.
print("|{:<10}|{:^15}|{:>10}|".format("Butter", "Bread", "Ham"))

# Old Style Formatting like sprintf() in C prog.
x = 1223.3456789
print("The value of x is %7.2f" %x)         # 7 total character, 4 before dot, dot itself, 2 after dot

# Common Python String Methods
print("MustafaKatipoglu".lower())
print("MustafaKatipoglu".upper())
print("Mustafa Katipoglu".split())                       # ['Mustafa', 'Katipoglu']
print("Mustafa".find("af"))                              # 4
print("Mustafa Katipoglu".replace("oglu","o\u011flu"))   # Mustafa Katipoğlu

