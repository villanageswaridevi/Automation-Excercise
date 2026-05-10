"""
lambda: Lambda is a ananomous function means nameless function, here function it will take arguments
and it will evaluate the single expression. lambda function we can define by using lambda keyword.

syntax: lambda arguments: expression

"""
a = 10
b = 20
result = lambda a, b: a+b
result_sub = lambda a, b: a-b
result_mul = lambda a, b: a*b

print(result(a, b))
print(result_sub(a, b))
print(result_mul(a, b))


# lambda function can also used in conditional statements

score = 40

result = lambda score: "Pass" if score>=35 else "fail"
print(result(score))
print(result(32))


"""
Zip: zip is a one of the inbuilt function it will combine the multiple sequences, iterables
it is single and based on the index positions values.
we can use list, string, set, tuple we can use to combine based on the index positions 
"""

"""
take a list and print even and odd numbers using lambda and filter
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = list(filter(lambda x: x%2==0, numbers))
odd_numbers = list(filter(lambda y: y%2!=0, numbers))
print("even numbers", even_numbers)
print("odd numbers", odd_numbers)

























