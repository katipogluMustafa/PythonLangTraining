# In one interpreter session, there will only be one None object
# True, False and None is implemented as singleton in python

# None is does evaluates to False
if None:
    print("This wont be printed")
else:
    print("But this will be")

# But None and False is not the same
if None != False:
    print("Sorry, None and False is not same:/")

if [] != None:
    print("Not equal to empty list too")

x = None
y = None
if x == y:
    print("Indeed, they are equal to each other")


# Any function that has no return will return None automatically
def initiate_splinter_sequence():
    a = "The target time has been locked"
    b = "Sequence has been started"
    c = "BB"
    print(a + b + c)


x = initiate_splinter_sequence()
if x == None:
    print("x is equal to None....")

# Lets see if x and None points to the same object
if x is None:
    print("x and None points to the same object")

if x is not None:  # Kinda ugly but here it is, not operator
    print("x is not points to the None")


# Another use is to give optional parameters to functions an 'empty' default

def spam(foo=None):
    if foo is not None:
        print("Do Something...\n")
    else:
        print("Sorry, foo is none")


spam("Something other than None")  # will print "Do Something"
spam()                             # will print "Sorry, foo is none"
