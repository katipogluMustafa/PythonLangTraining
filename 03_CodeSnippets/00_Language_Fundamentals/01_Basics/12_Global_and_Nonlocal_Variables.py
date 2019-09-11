## Nonlocal Variables

def outer():
    x = "local to outer"

    def inner():
        # nonlocal x        # if we uncomment then we refer to the same x as outer x
        x = "nonlocal"
        print("inner : ", x)

    inner()
    print("outer: ", x)

outer()

## Global Variables

# global keyword allows you to modify the variable outside of the current scope.
# It is used to create a global variable and make changes to the variable in a local context.
# Use of global keyword outside a function has no effect

c = 1

def add():
    global c
    c += 2
    print(c)

add()

# we can also declare global variables inside function

def mul(a,b):
    global result
    result = a * b

mul(5,8)
print(result)
mul(7,3)
print(result)

print(dir())