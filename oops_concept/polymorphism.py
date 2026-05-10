"""
Polymorphism: It means "many forms"
--> It allows one function or method to work in different ways by depending on the object calling it.
--> Polymorphism helps in writing flexible and reusable code.
--> Example: Imagine the word "draw":
    If a pencil draws → it draws a sketch
    If a printer draws → it prints a document
    If a paintbrush draws → it paints a picture
    Same action name (draw), but different behaviors based on the object.

method overring: once we have same method name in parent class and child class, if we create object
of the child class once we call the method it will executes child class method and parent class
method will be override.

method overloading: basically it won't support python directly we can achieve method overloading
in python by using default arguments

"""
# example 1
class Dog:
    def speak(self):
        print("Woof!")

class Cat:
    def speak(self):
        print("Meow!")

# Polymorphism in action
for animal in [Dog(), Cat()]:
    animal.speak()


# example
class HD:
    def get_bike_details(self, price=200000):
        print("bike details:", price)


obj = HD()
obj.get_bike_details()


# obj.get_bike_details(1900000)


# print even or odd and prime numbers from the list using multiple inheritance
# Parent class 1: Even and Odd logic
class EvenOdd:
    def check_even_odd(self, numbers):
        print("Even Numbers:")
        for num in numbers:
            if num % 2 == 0:
                print(num, end=" ")
        print("\nOdd Numbers:")
        for num in numbers:
            if num % 2 != 0:
                print(num, end=" ")
        print()


# Parent class 2: Prime number logic
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]


class Prime:
    def check_prime(self, numbers):
        print("\nPrime Numbers:")
        for num in numbers:
            if num > 1:
                for i in range(2, int(num ** 0.5) + 1):
                    if num % i == 0:
                        break
                else:
                    print(num, end=" ")
        print()


# Child class: Inherits both EvenOdd and Prime
class NumberChecker(EvenOdd, Prime):
    def __init__(self, numbers):
        self.numbers = numbers

    def process(self):
        self.check_even_odd(self.numbers)
        self.check_prime(self.numbers)


checker = NumberChecker(numbers)
checker.process()

