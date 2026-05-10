"""

special functions :
lambda, map, zip, reduce and filter
lambda: lambda is a special function it can be used to write a single line expression it is a anonymous
function, we can create in a line.
lambda function can take args and it will evaluate the expression.
this lambda function we can use any other special function.

syntax:
lambda args: exp
this function can store into an object how we can call the function object

"""
a = 10
print(a*a)
lambda_obj = lambda x:x*x

lambda_obj = lambda x,y:x*y
print(lambda_obj(10,20))

"""
map: map function is used to map the values for any function, generally map function
can take function argument and any sequence as a other argument and it will return map object, 
we can convert type casting.

syntax: map(fun,seq)

"""
def fun(x):
     print(x*x)
     return x*x
     l_obj = lambda x: x * x

     a = [1, 2, 3, 4]
     for i in a:
         fun(i)
         l1 = map(fun, a)
         print(l1)
         print(list(l1))


"""
 zip: zip function is used to zip the values based on the index positions, it will also return zip
 objects contains tuple values.

syntax: zip(seq1,seq2)

"""
l1 = [3, 7, 29]
l2 = [29,  30, 31]
z_obj = list(zip(l1, l2))
print(z_obj)

"""
# Reduce: reduce function is an argument and any seq as another arguments.
# syntax: reduce(fun,seq)

"""

from functools import reduce

a = [1, 2, 3]


def fun(i, j):
    return i * j

sum_of_vals = reduce(fun, a)
sum_of_vals = reduce(lambda i, j: i * j, a)
print(sum_of_vals)


"""
filter: It will take functions as args and any sequence is another argument, here filter can filter the value
based on the condition.
syntax: f_obj = filter(fun, seq)

"""

a = [1, 2, 3, 4, 5]
def is_even(i):
     return i%2==0
f_obj = filter(is_even, a)
f_obj = filter(lambda i: i%2==0, a)
print(list(f_obj))







