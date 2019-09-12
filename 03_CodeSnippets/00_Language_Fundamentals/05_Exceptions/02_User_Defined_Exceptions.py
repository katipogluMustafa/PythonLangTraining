# Custom Exception

class ServerNotFoundError(Exception):
    pass

try:
    raise ServerNotFoundError
except ServerNotFoundError as e:
    print("Error: ", type(e))

try:
    raise ServerNotFoundError("Server Connection Failed...")
except ServerNotFoundError as e:
    print(e)


class Error(Exception):
    """"Base class for other exceptions """
    pass

class ValueTooSmallError(Error):
    pass

class ValueTooLargeError(Error):
    pass

while True:
    try:
        i = int( input("Number") )
        if i < 10:
            raise ValueTooSmallError
        elif i > 10:
            raise ValueTooLargeError
        break
    except ValueTooSmallError:
        print("Value too small")
    except ValueTooLargeError:
        print("Value too large")

