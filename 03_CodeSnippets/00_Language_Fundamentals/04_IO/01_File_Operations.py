### File Operations

# f = open("test.txt")                # equivalent to 'r' or 'rt', r = read, t = text
# f.close()                           # file must exists in read mode

f = open("test.txt", "w")           # write in text mode, 'wt'
f.close()

f = open("img.bmp", "w+b")          # read and write in binary mode
f.close()

# specify encoding if you don't want the app behave different on different OS

f = open("test.txt", mode = "r", encoding = "utf-8")
f.close()


# In case of exception, you need to be careful about closing a file

try:
    f = open("test.txt", mode = "w+", encoding="utf-8")
    # do somethings
finally:
    f.close()

# with statement implicitly closes the file
with open("test.txt", encoding="utf-8") as f:
    # do some operations
    pass

# We need to be careful with the 'w' mode as it will overwrite into the file if it already exists. All previous data are erased.
# 'x'	Open a file for exclusive creation. If the file already exists, the operation fails.

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Selamu Aleykum\n")
    f.write("This is the second line of the file\n\n")

f = open("test.txt", "r", encoding="utf-8")
print( f.read(6) )              # first 6 characters, 'Selam'
print( f.read(8) )              # next 8 characters, 'u Aleykum'
print( f.read() )               # read until EOF
print( f.read() )               # Further reading will return empty string after reaching EOF

print("Position: ",f.tell(), "\n")                 # Position of internal file pointer
f.seek(0)                       # Set the file pointer to position 0
print(f.read())


# We can read line by line, in a efficient and fast way
f.seek(0)
for aline in f:
    print(aline, end="")

# Alternatively we can use readline()
f.seek(0)
print( f.readline() )

# Lastly, the readlines() method returns a list of remaining lines of the entire file.
# All these reading method return empty values when end of file (EOF) is reached.

f.seek(0)
print( f.readlines() )


# Get File descriptor
print( f.fileno() )

# Flush the write buffer of the file stream
f.flush()

#  Get info about stream
print( "File is readable : ", f.readable() )
print( "File Stream supports random access: ", f.seekable() )
print( "Stream is writable: ", f.writable() )