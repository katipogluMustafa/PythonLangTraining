# Functions

## Keyword arguments and default arguments must be at the end of argument list

def greet(name,msg="Good Morning!"):            # default argument at the end
    print("--", msg + ' ' + name)

greet("Mustafa", msg="Selamun Aleykum")         # Keyword argument at the end

## Variadic Functions

def greet(*names):
    """This function greets all the person in the names tuple."""
    # names is a tuple with arguments
    for name in names:
        print("Selamu Aleykum", name)

# Here, we have called the function with multiple arguments.
# hese arguments get wrapped up into a tuple before being passed into the function.
# Inside the function, we use a for loop to retrieve all the arguments back.

greet("Mustafa")
greet("Ahmet")
greet("Yusuf")

print()
