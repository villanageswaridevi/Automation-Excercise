"""
1. Arithemetic Operators
"""
from traceback import print_tb

a = 10
b = 20
print(a + b)
print(a - b)
print(a * b)
print(a / b)

"""
2. Conditional statements: 
if statement:
An if statement checks the condition, and runs the code only if the condition is true.
"""
age = 18
if age >= 18:
    print("Eligible for vote")

"""
else statement:
The else statement is run only if the condition is false. 
"""
# check positive or negative
num = 10
if num > 0:
    print("Positive integer")
else:
    print("Negative integer")

#  check even or odd
num = 7
if num % 2 == 0:
    print("Even number")
else:
    print("odd number")

"""
elif statement: 
The elif statement is also checks another condition when the previous if is false

break: 
The break is used to stop the loop immediately.

continue:
continue statement is skips the current iteration and moves to next one.

pass:
it does nothing, its just a placeholder,and it will avoid syntax error.  
"""

"""
3. Functions:
--> inbuilt functions:
once we install the python by default it will install.
print() - it will returns the output.
int() - convert into integers
min() - returns the minimum value
type() - it will returns what type of object it is.
dir() - it will returns all the available methods in the object or class.

--> user defined functions:
This function is defined by using def keyword.
And it is used to reuse the code and maintenance is easy
Types:
=====
1. Positional arguments: value assigned based on position
2. Default arguments: parameter has default value if not provided
3. *args: *args collects multiple positional arguments and store into tuple
4. **kwargs: Collects multiple keyword arguments and store into a dictionary

"""
#  Positional arguments:
def great(name, age):
    print(f"Name:{name}, Age: {age}")
great("Nageswari", 25)

# Default arguments:
def details(name,loc, course = "Python Automation"):
    print("Name:", name)
    print("Location", loc)
    print("Course:", course)
details("Nandha","yanam")

# *args:
def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Total:", total)
add_numbers(1, 2, 3, 4, 5)

# example 2:
def calculate(*args):
    add = sum(args)

    sub = args[0]
    for i in args[1:]:
        sub -= i
    print("Addition:", add)
    print("Substraction:", sub)
calculate(10, 1, 15)

# **kwargs:
def show_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

show_details(name="Nageswari", age=25, course="Python Automation")

"""
4. Special functions:
1. Lambda : 
--> Lambda function is defined by using lambda keyword.
--> And it is an Anonymous function and an nameless function.
--> and we can write in a single line expression, Lambda is used in all the special functions.
syntax: lambda expression : arguments 
"""

# example = 1
a = 10
b = 20
c = 30
d = 10
print((lambda a, b: a+b)(a, b))
print((lambda c, d: c-d)(c, d))

# example - 2 assign variable
a = 10
b = 20
addition = lambda a, b : a+b
print(addition(a, b))
substraction = lambda a, b :a-b
print(substraction(a, b))

# using conditional statements
score = 40
result = lambda score : "pass" if score>=35 else "fail"
print(result(score))
print(result(30))

"""
2. Map :
--> Map is an inbuilt function
--> Map function is used to map the values and it will take function as an argument and any sequence as another
argument and it will returns the map object and it will convert into list.
syntax : map(fun, seq)
"""

# example square of numbers
numbers = [1, 2, 3, 4, 5]
square = list(map(lambda x: x * x, numbers))
print(square)

# Example without using lambda
def square(x):
    return x * x
numbers = [10, 20, 30]
result = (list(map(square, numbers)))
print(result)

"""
3. Zip:
--> Zip is one of the inbuilt function it will combine the multiple sequences, iterables into a single
based on the index positions. / based on the index positions it will combine values.
--> In zip function we will use list, string, set, tuple.
--> And it will returns zip objects contains tuple values.
Syntax: zip(seq1, seq2, ......)

"""
# Example 1
l1 = ["a", "b", "c"]
l2 = ["apple", "ball", "cat"]
l3 = [1, 2]

result = list(zip(l1, l2, l3))
print(result)

"""
4. Reduce:
--> reduce function is used to apply the function cumulatively to the items in an iterables (like a list)
and it will produce a single result.
--> Cumulatively means adding or applying something step-by-step so that each step uses the result from the 
previous step.
--> and it will import from functools
"""

# Example 1 - Multiplying numbers

from functools import reduce

numbers = [1, 2, 3, 4]

result = reduce(lambda x, y : x * y, numbers)
result1 = reduce(lambda x, y : x + y, numbers)

print(result)
print(result1)

#  Example - 2 add the values using user defined functions.
# def add_values(a, b):
#     return a + b
# list = [1, 2, 3]
# print(reduce(add_values, list))

"""
5. Filter:
--> filter function we can used to get the values based on the condition.
syntax: filter(fun, seq) -- in sequence we can use any iterables like list, set, tuple, string..
--> and filter it will returns only truth values

"""

# Example 1
ages = [28, 32, 22, 40, 30]

def get_age(age):
    if age >= 25:
        return True
    else:
        return False

print(list(filter(get_age, ages)))

# Example 2: print even numbers
list1 = [1, 2, 3, 4, 5, 6, 7, 8]

result = list(filter(lambda x: x % 2 == 0, list1))
print(result)

# Example 3 without using lambda function
def even(num):
    return num % 2 == 0
nums = [1, 2, 3, 4, 5, 6, 10]
result = list(filter(even, nums))
print(result)

"""
4. Iterator:
--> It is a function any sequence we make it iterator by using iter function.
--> Iterator can hold only object reference because that size is less and 
it will returns one at a time by using next() method
--> We can utilize memory properly, and here the iterators are lazy calling.
--> Once we get all the values from the iterator it will throw stop iteration exception.
Syntax:
Iterator = iter(variable)
next(Iterator)
"""
# Example 1
numbers = [10, 20, 30, 40, 50]
iterator = iter(numbers)
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))
print(next(iterator))


# Example 2
string = "Nandha"
word = iter(string)
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))
print(next(word))

# Example 3 adding numbers
add = [1, 2, 3, 4]
addition = iter(add)
total = 0

total += next(addition)
total += next(addition)
total += next(addition)
total += next(addition)

print("sum:", total)


"""
Generator:
--> generators are used to create the iterators in a simple way and we can use yield keyword instead of 
return in a function.
--> We can use next() method to call the generator object.
--> and we can utilize memory properly.
"""

# Example 1
def seq_numbers(n):
    for i in range(n):
        yield i * i

obj = seq_numbers(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

# Example 2

def get_numbers(n):
    yield n * 1
    yield n * 2
    yield n * 3
    yield n * 4
    yield n * 5

obj = get_numbers(5)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


"""
Decorator:
--> Decorator is a function and it is used to adds the extra functionality to the another function 
without changing its original code.
--> And it will take function as an argument and we have inner/wrapper function inside decorator we can apply any
function by using @notation.
"""

# Example 1
def dec_function(func):
    def inner():
        print("It's weekend")
        func()
    return inner

def dec_festival(func):
    def inner():
        print("Let's we celebrate festival")
        func()
    return inner

@dec_function
@dec_festival
def normal_fun():
    print("routine work start")
normal_fun()


"""
5. File Handling:
open(): by using open method we can perform file operations.
with open(): by using this method we can perform file operations.

file modes:
w: write -> if the file is not there it will create the file and write the data,
if the file is already exists it will override the data.
write(): We can used to write a single line
writelines(): we can write multiple lines in a form list
read: it will read all the data into single string
readline: it will read only one line at once.
readlines: it will read all lines and it will return list of lines.
r: read -> if the file is there it will read the data otherwise it will throw the exception 
like file not found error.
a: append -> it will append the data at end of the file / it will add the data at end of the file.


"""
# Example 1
obj = open("demo.txt", "w")
obj.write("Hello I am learning python file handling from the beginning \n")
obj.write("After that I need to learn exception handling \n")
obj.writelines(["Third line \n", "Fourth line \n", "Fifth line \n"])
obj.close()

# Example 2
def write_file_with_data(filename, mode):
    try:
        obj = open(filename, mode)
        obj.write("Learning python file handlings along with exception handling mechanism.")
    except PermissionError as e:
        print("got exception:", e)
    except FileNotFoundError as e:
        print("File is not there", e)

    finally:
        obj.close()

write_file_with_data("learn.txt", "w")

"""
6. Exception handling:
--> Exception handling is a way to handle runtime errors so that the program does not crash 
and continues normally. 
--> And we can use try, except, else, finally keywords

Syntax: 
try:
# code
We can write main logic here

except:
# code
We can handle those exceptions here

else:
# code
only some times we can use this block

finally:
always executes the code
"""

# Example 1 using try, except, else


try:
    a = 10
    b = 0
    result = a / b
except ZeroDivisionError:
    print("Divided by zero error")
else:
    print("Result is:", result)
finally:
    print("Execution is completed")


"""
7. Package:
--> Package is a folder or directory and it will contains multiple python files
--> It will group the multiple modules into a single package.
--> And it contains __init__.py file it may be empty or we can write something

Example: 

# Package Structure:

my_package/         --> Package(folder)
    __init__py      --> It may be empty or we can write something
    add.py          |
    sub.py          | --> add.py and sub.py modules inside the package
main.py             --> We can write main program here


# add.py

def addition(a, b):
    return a + b
    
# sub.py

def substraction(a, b):
    return a - b
    
# main. py

from my_package import add, sub
print(addition(10, 5))
prnt(substraction(15, 10))

Output: 15, 5

Explanation: 
--> my_package contains two modules add and sub
--> main.py imports modules from the package
--> The functions performs addition and substraction

"""

"""
8. Module:
--> Module is a file that contains python code such as functions, classes, or variables which can 
reuse in other programs by using import.

# Example:
math_operations.py
def add(a, b):
    return a + b
    
def sub(a, b):
    return a - b
    
# main program

import math_operations

print(math_operations.add(10, 5))
print(math_operations.sub(10, 5))

# Output:
15
5

"""


"""
9. OOP's concept:
--> It is an object oriented programming language 
--> This is the way of organising programs by using classes and objects.
--> oops makes programs easier to understand, maintain, and reuse the code.

Class: 
--> class is a blue print of an object it will represents the realtime properties, attributes and class can 
contains methods, variables, attributes etc..

object:
--> object is used to create the object of the class by calling the class name.

self:
--> Self represents the reference object, it will be the first argument of an class function  

__init__:
--> It is a constructor 
--> This is a special method in python classes.
--> It runs automatically when you create object of the class.
--> The main purpose is to initialize the objects data/variables.

super() method:
--> super() method in python is used to call the methods of the parent(super) class inside the child class

Types of oop's:
1. Inheritance:
--> Inheritance is used to reuse the code, to make programs easier to maintain and to implement 
the real world relationships like (parent & child)

Types of Inheritance:
1. Single inheritance: single parent & single child
2. Multiple inheritance: one child inherits from multiple parents.
3. Multi-level inheritance: child of child means one child class inherits from another child class
4. Hierarchical inheritance: one parent multiple child classes means 
multiple child classes inherits from one parent 
5. Hybrid: combination of all above.


2. Polymorphism:
--> It means many forms
--> Polymorphism means one function or method can work in different ways.

Types:
1. method overriding:
--> Once we have same method name in parent class and child class , if we create object of the 
child class once we call the method it will be executes the child class method and
parent class will be override.

2. method over loading:
--> Basically it won't support python file directly we can achieve over loading in python 
by using default arguments.


3. Abstraction:
--> abstraction is used to hide the internal implementation only it will expose necessary details of the object.
--> abstraction we can achieve by using ABC module and we can create the abstract method.
--> And we cannot create object of the abstract class.

4. Encapsulation:
--> In encapsulation we can hiding the data into a single unit.
--> We can provide security to the variables, functions etc..

Types of encapsulation:
1. Public:
--> It can accessible within the class, sub class, and outside of the class

2. Private:
--> private it can be access within the class and subclass.
--> private we can access outside of the class by using name mangling.
--> variables/ methods starts with double under (__)score.

3. Protect:
--> variables/ methods marked with a single under score (_)
--> This can be access within the class, sub class and outside of the class with object reference.


"""

# Single Inheritance example:
class A:
    def show(self):
        print("parent class")
class B(A):
    pass

obj = B()
obj.show()

#  example code for Polymorphism:
def add(a, b):
    return a + b

print(add(5, 10))
print(add("hello", "world"))

# example for Abstraction:

from abc import ABC, abstractmethod

class shape(ABC):

    @abstractmethod
    def area(self):
        pass

class square(shape):
    def area(self):
        print("Area of square")

obj = square()
obj.area()





class parentclass:
    def tenth(self):
        print("tenth class pass")
class parentclass2:
    def inter(self):
        print("inter passed")

class child(parentclass, parentclass2):
    def answer(self):
        print("All clear")

obj = child()
obj.tenth()
obj.inter()
obj.answer()








# # type casting
# a = 10
# print(str(a))
#
# # str can convert into list, tuple, set and if str only contains digits we can convert into int as well
#
# s1 = "100"
# print(int(s1))
# l = [1, 2, 3]
# # list can convert into str, tuple, set
# # tuple can convert into str, list and set
# # set can convert into str, list and tuple
# print(len(str(l)))
# print(len(tuple(l)))
#
# t = (1, 2, 3)
# print(str(t))
#
# # how to declare empty and single object
#
# # t1 = (10,)
#
# # for loop
#
# s = "MSN"
# l = [1, 2, 3, 4, 5]
#
# for i in s:
#     for j in l:
#         print(i, j)
#
#
#
# s1 = "msn python automation testing"
# # find all the vowels and their counts
# # each character count
# # find the words in a string
#
#
# """
# find even / odd numbers from the list
# """
# l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []
#
# for i in l:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print("Even Numbers:", even)
# print("Odd Numbers:", odd)
#
#
# """
# find even index values from the list
# """
# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_index = []
# for i in range(len(l)):
#     if l[i]%2==0:
#         even_index.append(i)
# print("Even index position:", even_index)
#
#
# """
# s1 = "msn s"
# output = {"m": 1, "s": 2, "n": 1, " ": 1
# """
#
# for i in range(65, 91):
#     for j in range(65, i+1):
#         print(chr(j), end= " ")
#     print()
#
# for i in range(1, 5):
#     for j in range(1, i+1):
#         print("*", end=" ")
#     print()
#
# for i in range(1, 20):
#     if i%2==0:
#         for j in range(2, i+2, 2):
#             print(j, end=" ")
#         print()
#
#
# for i in range(1, 10):
#     if i % 2 != 0:
#         for j in range(1, i+1, 2):
#             print(j, end=" ")
#         print()
#

print("Hello World")




























