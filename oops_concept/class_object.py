"""
OOPs: (object oriented programming system) is a programming concept that organizes code
using class and object. Python is a object oriented language.

Class : A blueprint of an object, it will represents the realtime properties, attributes
class can contains methods, variables, attributes etc.
Object : We can create the object of the class by calling class.
Self : represents the class reference object, it will be the first argument of the class functions.
Constructor : __init__() we can say constructor it will take self as a first argument,
constructor will execute once we create object of the class.
Inheritance :
Polymorphism :
Encapsulation :
Abstraction :




"""

class Interview: # I have created the class, by using class keyword / class declaration
    name = "Nandhu"  # I have declared a name variable / Attribute or variable

    def __init__(self, name, course, duration): # this we can say constructor and it will take 3 args
        # these 3 args can say instance attributes
        print("init execution started")
        self.name = name
        self.course = course
        self.duration = duration
        print(self.name, self.course, self.duration)
        print("init execution completed")

    def first_round_tech(mad, name):  # I have defined a function by using def keyword with function name
        print(" hello world")
        # or fun, self is a class reference object
        # pass  # just I have created the empty function that's why I'm using pass statement


obj = Interview("msnpython", "python", "40 days") # I have created obj by calling
# class name / creating obj of the class by calling the class
# obj.first_round_tech("Nandhu") # using the obj by calling the function name /
# by using obj calling fun, no need to provide self.
# the main purpose of the constructor if you want to initialize the any attributes at the time we can use
# constructor. Initialization means declaring the variables


