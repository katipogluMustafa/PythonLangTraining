## Execution Mode Detection

# When a .py file is imported as a module, Python sets the special variable __name__ to the name of the module.
# However, if a file is run as a standalone script, __name__ is (creatively) set to the string '__main__'.

if __name__ == '__main__':
    print("Executing as standalone scipt not as module"
          "You can put any debug output by checking like this")


## Reloading a module
# If you make a change to a module and need to reload it, you need to either restart the interpreter or use a function called reload() from module importlib
import math

import importlib
importlib.reload(math)


