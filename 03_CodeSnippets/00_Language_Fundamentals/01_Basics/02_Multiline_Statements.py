# Multiline Statements

# Explicit multiline statements
a = 1 + 2 + \
    3 + 4 + \
    5 + 6
print(a)

# Implicit multiline statements

a = (1 + 2 + 3 + 4
     + 5 + 7 + 8 + 9)
print(a)

colors = ['blue', 'green'
          'black', 'white']
# line continuation is implied inside parentheses ( ), brackets [ ] and braces { }

# Multiple Statements in a line

a = 1; b = 3; c = 4;
print( a + b + c)