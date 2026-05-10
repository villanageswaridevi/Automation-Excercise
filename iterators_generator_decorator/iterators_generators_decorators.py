# a = ([1, 2, 3, 4,5])
# print(a.__sizeof__())
"""
Iterators: It is a function any sequence we make it a iterator by using iter function.
Iterator can hold only object reference because of that size is less.
we can utilize memory properly, here iterators are lazy calling.
once we get all the values from the iterator it will throw stop iteration exception.

syntax: iter(1, 2, 3)
"""
# b = iter(a)
b = iter([1, 2, 3, 4, 5])
print(type(b))
# print(b.__sizeof__())
print(next(b))
print(next(b))
print(next(b))
print(next(b))
print(next(b))
# print(next(b))


"""
Generators: generators are used to create iterators in simple way and we can use yield keyword to
the value instead of return in a function.
we can use next method to call generator object.
memory will be utilize properly.
"""

def seq_numbers(n):
     for i in range(n):  # start, stop, step
        yield i*i
         
obj = seq_numbers(10)
# print(type(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))

def get_numbers(n):
    yield n*1
    yield n*2
    yield n*3
    yield n*4

obj = get_numbers(10)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))


"""
decorators: it is a function and it will take as a arg we can have inner / wrapper function 
inside the decorator we can apply any function by using @ notation

Decorator is a function it is used to add extra functionality to another function without changing
its original code.

"""



# Example

def dec_fun(fun):
    def inner():
        print("It's weeked")
        fun()
    return inner

def dec_festival(fun):
    def inner():
        print("celebrate festival")
        fun()
    return inner

@dec_fun
@dec_festival
def normal_fun():
    print("Routine work")
normal_fun()



"""
Example 2
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
        print("how are you")
        fun()
        print("are you ok")
    return wrapper

@decorator
def mr():
    print("nandhu")
mr()


"""
Example 3 with festive names
"""
def dec_fun(fun):
    def inner(festive_name):
        print("It's weeked")
        fun(festive_name)
    return inner

def dec_festival(fun):
    def inner(festive_name):
        print("celebrate {} festival".format(festive_name))
        fun(festive_name)
    return inner

@dec_fun
@dec_festival
def normal_fun(festive_name):
    print("Routine work")
normal_fun(festive_name="Dasara")
normal_fun(festive_name="Deepavali")


"""
addition of 2 numbers and subtraction
"""
def num_fun(a, b):
    pass

def dec_add(fun):
    def inner(a, b):
        print(a+b)
        fun(a, b)
    return inner

def dec_sub(fun):
    def inner(a, b):
        print(a-b)
        fun(a, b)
    return inner

@dec_add
@dec_sub
def num_fun(a, b):
    pass
num_fun(10, 20)


c = iter([1, 2, 3, 4])
print(next(c))
print(next(c))
print(next(c))
print(next(c))
# print(next(c))
























