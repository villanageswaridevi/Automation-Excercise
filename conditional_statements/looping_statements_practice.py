# while loop:

# print 1 to 10 numbers
i = 1
while i <= 10:
    print(i)
    i += 1

# print 1 to 10 even numbers
i = 2
while i <= 10:
    print(i)
    i += 2

#  print sum of 1 to 10 numbers
i = 1
total = 0
while i <= 10:
    total += i
    i += 1
print("total sum", total)



t = (1, 2)
l = [1, 2, 3]

for i in l:
    print("outer for loop", i)
    for j in t:
        print("inner for loop:", j)

"""
print * pattern
"""
# n=int(input("enter a number:"))
# for i in range(1,n+1):
#     print('* '*i)

"""
another model to print star
"""
for i in range(5):
    for j in range(i):
        print("*", end = ' ')
    print()

"""
print * decresing
"""

for i in range (6): # rows
    for j in range(6-i): # columns
        print("*", end = ' ')
    print()

"""
print * pattern in pyramid shape
"""
for i in range(6):
    for k in range(6-i):
        print("", end = " ")
    for j in range(i):
        print("*", end = " ")
    print()

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


# n = input("enter no.of rows:")
#
# #
# for i in range(1, int(n)):
#     for j in range(1, i+1):
#         print("*", end = " ") # it will prevent new lines
#     print()


# slicing: to get the values based on index positions
# start:step:step
# start is included
# stop is excluded
# step is skip the values based on step value
l = [1, 2, 3, 4]
print(l[0])
print(l[0:2])
print(l[0:2:2])

print(l[-1])
print(l[-3:-1])
print(l[0::2])
print(l[::])
print(l[::2])
print(l[:2])
print(l[-1])
print(l[-3])
print(l[-3:])
print(l[-3:-2])
print(l[-3:-1])
print(l[::-2])
print(l[::-4])
print(l[-4:-2])



# n = input("enter:")
# for i in range(int(n), 0, -1):
#     for j in range(1, i+1):
#         print("*", end = " ") # it will prevent new lines
#     print()


"""
sort the list using inbuilt
"""
# l1 = [1, 2, 3, 4, 5]
# l2 = [5, 4, 3, 2, 1]
# l3 = [4, 3, 5, 1, 2]
#
# l3.sort()
# print(l3)
# l3.sort(reverse=True)
# print(l3)


"""
without using inbuilt
"""

l = [6, 7, 4, 3]


# def sort_list(l):
n = len(l)
for i in range(n):
    for j in range(0, n-i-1):
        if l[j]>l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
print(l)


a = 0
b = 1
for i in range(10):
    c = a+b
    a, b= b, c
    print(a)



# while loop we can use based on condition

# l = [1, 2, 3, 4]
c = 0
while c<10:
    print(c)
    c+=1


# fibonacci series
# end method is used to print in the same line

# a, b =  0, 1
# counter = 0
# n = 15
# while counter<n:
#     print(a, end = " ")
#     c = a + b
#     a, b = b, c
#     counter += 1



# print even number from the list using for loop

l = [1, 2, 3, 4, 5, 6]
for i in l:
    if i%2==0:
        print(i)



# print even number from the list using while loop
#  so while loop until condition is true it will executed, once condition is false it will come out of the loop

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

counter = 0
while counter<len(l):
    if l[counter]%2==0:
        print(l[counter])
    counter+=1
print("after while loop complete")

# print which is divisible by 3 and 5

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]
for i in l:
    if i%3==0 and i%5==0:
        print(i)

# take a list and print which is divisible by 3 and 5
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15]

counter = 0
while counter<len(l):
    if l[counter]%3==0 and l[counter]%5==0:
        print(l[counter])
    counter+=1
"""
1. for loop basics with examples?
2. while loop with examples?
3. find even numbers in a list using for and while loop?
4. prime number and fibonacci with for and while loop?
5. palindrome, anagram, reverse number?
6. take a=121 print palindrome?
7. print only anagram take a list l = ["ate", "eat", "bat", "cat"]
8. pattern programs?
9. get all the numbers from 1 - 100 which is divisible by 4 and 7? complete
10. range function?
11. slicing with loop?

"""


# get all the numbers from 1 - 100 which is divisible by 4 and 7?
l = []

for i in range(1, 101):
    if i%4==0 and i%7==0:
        l.append(i)
print("divisible by both 4 and 7:", l)

# get all the numbers from 1 - 100 which is divisible by 4 and 7? using while loop

i = 1
while i<=100:
    if i%4==0 and i%7==0:
        print(i)
    i+=1


# take a=121 print palindrome?

"""
Break: we can use to terminate current loop based on the condition, 
once break is executed  it won't execute any piece of code inside loop
continue: we can use to skip the current iteration based on the condition
pass: we can use to avoid syntax error for defining empty classes, functions
"""

# break example
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l:
    # print("i value before break:", i)
    if i == 4:
        break
        print("i after break")
    print("After if condition", i)
print("After for loop:", i)

c = 0

while c<5:
    print("c value before break:", c)
    if c==3:
        break
        print("break")
    print("c value after if condition", c)
    c+=1
print("c value outside while loop", c)





l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in l:
    if i==4 or i==6:
        continue
        print("hello continue")
    print("I value:", i)


# continue statement
c=0
while c<len(l):
    # c+=1
    if l[c]==4:
        # print("if condition value:", l[c])
        # c+=1
        continue

        print("value:", l[c])
        c+=1


# pass example

while True:
    pass

for i in range(10):
    pass























