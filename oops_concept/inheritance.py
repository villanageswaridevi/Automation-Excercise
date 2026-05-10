"""
Inheritance : Inheritance is a feature Object-Oriented programing that allows one class to
acquire properties and methods of another class.

why use inheritance?
--> to reuse the code.
--> to make the programs easier to maintain.
--> to implements real-world relationships.(like parent - child)

Types of inheritance:
Single : one parent, one child
multiple : one child inherits from multiple parents
multilevel : child of child
Hierarchical : one parent, multiple children
Hybrid : combination of above types

"""
from traceback import print_tb


# single Inheritance :
class parent: # parent class
    def question(self):
        print("Hello dear how are you?")

class child(parent):  # child class
    def answer(self):
        print("Fine daddy")

obj = child()
obj.question()
obj.answer()

# multiple Inheritance:
class parent1:
    def question1(self):
        print("Hello dear how are you?")
class parent2:
    def question2(self):
        print("Are you ok?")

class child(parent1, parent2):
    def answer(self):
        print("Yeah, I'm fine")

obj = child()
obj.question1()
obj.question2()
obj.answer()


# multilevel Inheritance:
class grandpa: # Grandfather class
    def property(self):
        print("Grandpa's land")

class parent(grandpa): # parent class
    def house(self):
        print("House property")

class child(parent): # child class
    def job(self):
        print("I'm well settled")

obj = child()
obj.property()
obj.house()
obj.job()

# Hierarchical Inheritance :
class parent: # parent class
    def land_property(self):
        print("lands available: which land you want")

class children1(parent): # child class
    def house_property(self):
        print("Elder son says: I want farming land.")

class children2(parent): # child class
    def banglow(self):
        print("Younger son says: I want national highway site.")

obj = children1()
obj.land_property()
obj.house_property()

obj = children2()
obj.land_property()
obj.banglow()


# Hybrid Inheritance : combination of multiple and multilevel
class Animal:
    def sound(self):
        print("Animals make sounds")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):  # Cat should not inherit from Dog here
    def meow(self):
        print("Cat meows")

class Tiger(Dog, Cat):  # Multiple inheritance: no conflict now
    def both(self):
        print("Tiger can make sounds and bark")

obj = Tiger()
obj.sound()   # From Animal
obj.bark()    # From Dog
obj.meow()    # From Cat
obj.both()    # From Tiger


# MRO : Method Resolution Order --> left to right
# When you have a class that inherits from multiple classes, and the same method or
# attribute exists in more than one parent, Python uses MRO to decide which one to pick first.

class mart:
    def items(self):
        print("All items")

class groceries(mart):
    def items(self):
        print("Dal, Oil")

class clothes(mart):
    def items(self):
        print("jeans, shirts, kurthies")

class kidsware(groceries, clothes):
    def items(self):
        print("jubbas, daipers, tissues")

obj = kidsware()
obj.items()


# another example

class RF:
    def __init__(self, year, model):
        self.year = year
        self.model = model

    def get_model_details(self):
        print("RF 2024")

    def price(self):
        print("price of RF")

class FZ:
    def model(self):
        print("FZ 2025")

    def price(self):
        print("price of FZ")

class Bikes(RF, FZ):
    def model(self):
        print("New bikes models")

    def brand(self):
        print("Latest brands")

obj = Bikes(2025, "HD")
# obj.model()
obj.get_model_details()





