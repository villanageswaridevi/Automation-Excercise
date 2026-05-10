"""
iterator: is a function, is used to create by using iter(), and we can use next() method
"""
l = [1, 2, 3, 4]
print(l.__sizeof__())
iter_object = iter(l)
print(iter_object.__sizeof__())
print(type(iter_object))
print(next(iter_object))
print(next(iter_object))
print(next(iter_object))
print(next(iter_object))
# print(next(iter_object))

"""
generator: is a function it will return the values using yield keyword  
"""
def numbers(n):
    yield n*1
    yield n*2
    yield n*3

obj = numbers(5)
print(next(obj))
print(next(obj))
print(next(obj))

# range:
obj = range(1, 11)
for i in obj:
    print(i)

def one_to_hundred():
    for i in range(1, 101):
        yield i

for k in one_to_hundred():
    print(k)


"""
decorators: it is a function and it will take as a arg we can have inner / wrapper function inside the decorator
we can apply any function by using @ notation
"""

def function(fun):
    def inner():
        print("welcome to python training")
        fun()
    return inner

@function
def fun():
    print("welcome to banglore")
fun()

def decorator(fun):
    def wrapper():
        print("miku nenu ante")
        fun()
        print("estam?")
    return wrapper

@decorator
def mr():
    print("entha")
mr()



"""
take a list to print even numbers
"""
def even_numbers(a):
    for i in range(a + 1):
        if i%2==0:
            yield i
for num in even_numbers(20):
    print(num)

"""
write a program to print multiple statements
"""
def function(fun):
    def inner():
        print("enti")
        fun()

    return inner


@function
def fun():
    print("thinara ji")


fun()

"""
another example
"""
def decorator(fun):
    def wrapper():
        print("call me")
        fun()
        print("when your free")

    return wrapper


@decorator
def fun():
    print("dear")


fun()

"""
add header & footer 
"""
def head_foot(fun):
    def inner():
        print("======Header======")
        fun()
        print("======Footer======")

    return inner


@head_foot
def hi():
    print("Full busy anukunta")

hi()

"""
print current time
"""
import time


def current_time(fun):
    def wrapper():
        print("current time is:", time.ctime())
        fun()

    return wrapper


@current_time
def fun():
    print("python ante siva siva ante python")


fun()


"""
print word twice
"""
def twice_word(fun):
    def inner():
        fun()
        fun()
    return inner
@twice_word
def func():
    print("hello ji")
func()

"""
decorator with arguments
"""
def arguments(fun):
    def inner(name):
        print("hi", name)
        fun(name)
    return inner
@arguments
def args(name):
    print("how are you", name)
args("ji")

"""
take a list to print positive and negetive integer
"""

def pos_neg(func):
    def inner():
        num = func()
        for i in num:
            if i < 0:
                print(f"{i} positive integer")
            elif i > 0:
                print(f"{i} negative integer")
            else:
                print(f"{i}zero")

    return inner
@pos_neg
def fun():
    return [1, 2, 3, -1, -2, -3]
fun()




















