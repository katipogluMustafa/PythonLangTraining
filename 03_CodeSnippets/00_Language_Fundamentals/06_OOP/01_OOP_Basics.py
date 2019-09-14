# OOP

class Parrot:
    species = "bird"            # class attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # instance methods
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self):
        return "{} is now dancing.".format(self.name)

blu = Parrot("Blue",12)
woo = Parrot("Woo", 15)

# Access class attributes
print("Blue is a {}".format(blu.__class__.species))         # Blue is a bird
print("Woo is also a {}".format(woo.__class__.species))     # Woo is also a bird

# Access instance attributes
print("{} is {} years old".format(blu.name, blu.age))       # Blue is 12 years old
print("{} is {} years old".format(woo.name, woo.age))       # Woo is 15 years old

# Call instance methods
print(blu.sing("Happy"))
print(woo.dance())
print()

# parent class
class Bird:
    def __init__(self):
        print("Bird is ready")

    def who_is_this(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class

class Penguin(Bird):
    def __init__(self):
        super().__init__()              # call parent constructor
        print("Penguin is ready")

    def who_is_this(self):
        print("Penguin")

    def run(self):
        print("Run faster")

peggy = Penguin()
peggy.who_is_this()
peggy.swim()
peggy.run()
print()


# Encapsulation

    # In Python, we denote private attribute using underscore as prefix i.e single “ _ “ or double “ __“.

class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print("Selling Price {}".format(self.__max_price))

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()

c.set_max_price(1100)
c.sell()

# Polymorphism

class MelopsittacusUndulatus(Bird):
    def fly(self):
        print("Melopsittacus Undulatus Can Fly")

    def swim(self):
        print("Melopsittacus Undulatus Can't Swim")

class Psittaciformes(Bird):
    def fly(self):
        print("Psittaciformes Can Fly")

    def swim(self):
        print("Psittaciformes Can't Swim")

    # Common interface
def flying_test(bird):
    bird.fly()

    # instance objects
x = MelopsittacusUndulatus()
y = Psittaciformes()

    # passing the objects
flying_test(x)
flying_test(y)