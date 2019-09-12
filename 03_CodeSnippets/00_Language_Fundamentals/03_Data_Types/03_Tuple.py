## Tuple

classic_tuple = (1, 3, 5, 7, 9)         # (1, 3, 5, 7, 9)
print(classic_tuple)                    # can not change items of a tuple

mixed_tuple = ( "Hello", 1, 2.0)
print(mixed_tuple)                      # ('Hello', 1, 2.0)

free_style_tuple = 3, 4, 5              # parenthesis are optional
print(free_style_tuple)                 # (3, 4, 5)

free_style_tuple2 = "Selam", 5,0, 1
print(free_style_tuple2)                # ('Selam', 5, 0, 1)

a, b, c = free_style_tuple              # tuple unpacking
print(a)                    # 3
print(b)                    # 4
print(c)                    # 5



# One Element Tuple

my_tuple = ("Hello",)                           # you must add trailing comma,
# otherwise it will be in this case string
print("Type of my_tuple is ", type(my_tuple))   # Type of my_tuple is  <class 'tuple'>

mystr = ("Another Hello")                       # no trailing comma, no tuple
print("Typeof mystr is ", type(mystr))          # Type of free_one  <class 'tuple'>

free_one = 1,
print(  "Type of free_one " , type(free_one) )  # Type of free_one  <class 'tuple'>

