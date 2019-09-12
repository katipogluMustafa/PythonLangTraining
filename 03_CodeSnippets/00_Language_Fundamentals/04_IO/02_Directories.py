import os

print( "Current Working Directory: ", os.getcwd() )

# Change Directory
os.chdir("C:\\Dev");
print( os.getcwd() )

# List Directories and Files
print( os.listdir() )               # no param prints current working directory
print( os.listdir("C:\\") )

# Create new directory
os.chdir("C:\\Users\\Yukawa\\PycharmProjects\\Project_1")
os.mkdir("test")
print(os.listdir())

# Renaming
os.rename("test", "new_test")

# Remove empty directory
os.rmdir("new_test")

# Remove a file
if "test.txt" in os.listdir():
    os.remove("test.txt")

# Remove non-empty directory
os.mkdir("test")
os.chdir("test")
with open("deneme.txt", "w+", encoding="utf-8") as file:
    file.write("Just some text")
os.chdir("..")
print(os.getcwd())

import shutil
shutil.rmtree( "test" )             # remove non-empty directory



