# Exceptions

import sys

ran_list = ['a', 0, 2]

for i in ran_list:
    try:
        print("The entry is ", i)
        r = 1/int(i)
        break
    except:                 # Catch all types of exceptions
        print("Whups!", sys.exc_info()[0], "occured.")
        print("Next entry.\n")


# Catching Specific Exception

try:
    # do something
    pass
except ValueError:
    # Handle
    pass
except (TypeError, ZeroDivisionError):
    # Handle multiple exceptions
    pass
except:
    # handle all the other exceptions
    pass

# Throwing Exception
try:
    raise KeyboardInterrupt
except KeyboardInterrupt:
    print("Handling KeyboardInterrupt...")

# Add Notes to the exception
try:
    raise MemoryError("Full Memory...")
except MemoryError:
    print( sys.exc_info() )
    # (<class 'MemoryError'>, MemoryError('Full Memory...'), <traceback object at 0x02FCEAD0>)

try:
    a = int( input("Number: ") )
    if( a <= 0):
        raise ValueError("Non-negative Number is Required")
except ValueError as neg_ex:
    print(neg_ex)                   # prints "Non-negative Number is Required"


# try ... else

try:
    f = open("test.txt", encoding="utf-8")          # on error, f never gets defined
    # do somethings
except FileNotFoundError:
    pass
else:    # else instead of finally                   # if no error, this will be executed
    f.close()

# if we used finally, in case of error, f never gets defined, another exception occurs inside finally block