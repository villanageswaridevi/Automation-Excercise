# uses of end
from operator import truediv

print("hello world", end = ' ')
print("hi")


"""
print * pattern
"""
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print('* '*i)

"""
another model to print star
"""
# for i in range(5):
#     for j in range(i):
#         print("*", end = ' ')
#     print()

"""
print * decresing
"""

# for i in range (6): # rows
#     for j in range(6-i): # columns
#         print("*", end = ' ')
#     print()

"""
print * pattern in pyramid shape
"""
# for i in range(6):
#     for k in range(6-i):
#         print("", end = " ")
#     for j in range(i):
#         print("*", end = " ")
#     print()

"""
print numbers in line by line
"""
count = 1
for i in range(1, 6):
    for j in range(i):
        print(count, end = ' ')
        count += 1
    print()


"""
print a triangle pattern in simple way
"""
for i in range(1, 6):
    print("* "* i)

"""
print largest of 3 numbers
"""
a = 10
b = 15
c = 12
print("largest of 3 numbers:", max(a, b, c))

"""
sum of list
"""
a = [1, 2, 3, 4, 5]
print("sum:", sum(a))

"""
positive and negative integers
"""
l = [1, -9, 4, -5, 5, 0]
pos = 0
neg = 0
zero = 0
for i in l:
    if i > 0:
        pos += 1
    elif i < 0:
        neg += 1
    else:
        zero = 0

print("positive integers are:", pos, "\nnegative integers are:", neg, "\nzeros are:", zero)

"""
reverse the number
"""
n = 1234
rev = 0
while n > 0:
    rev = rev * 10 + n % 10
    n = n // 10
print("Reversed:", rev)


"""
diamond shape * stars
"""
rows = 3

for i in range(1, rows + 1):
    print(" " * (rows - i) + "* " * i)

for i in range(rows - 1, 0, -1):
    print(" " * (rows - i) + "* " * i)


"""
print given string is a palindrome ar not
"""
# def is_palindrome(s):
#     return s==s[::-1]
# s = input("enter a string:")
# if is_palindrome(s):
#     print("is a palindrome")
# else:
#     print("Is not a palindrome")

"""
prime numbers
"""
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, n//2+2):
        if n%2==0:
            return False
        else:
            return True
n=int(input("enter a number:"))
print(is_prime(n))









