# write a program to print common prefix

import os
l = ["flower", "float", "flag", "flavour"]
x = os.path.commonprefix(l)
print(x)

# most important program in python
# print prime numbers from the list

numbers = [2, 3, 4, 5, 6, 7, 8]
for num in numbers:
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            print(num, "is a prime number")

# another type to print prime numbers
# n = int(input("enter a number:"))
# if n > 1:
#     for i in range(2, n//2+1):
#         if n%i==0:
#             print("It's not a prime number")
#             break
#     else:
#         print("It's a prime number")
#

# print positive, negative integer or zero

# num = int(input("Enter the number:"))
# if num>0:
#     print("positive integer")
# elif num==0:
#     print("zero")
# else:
#     print("negative integer")

# print positive, negative integer or zero from the list

l = [1, 2, 3, -2, -3, 0]
pos = []
neg = []
zero = []
for i in l:
    if i>0:
        pos.append(i)
    elif i==0:
        zero.append(i)
    # else
        neg.append(i)
print("positive integers are:", pos)
print("negative integers are:", neg)
print("zero:", zero)


# print even or odd
# num = int(input("enter the number:"))
# if num%2==0:
#     print("{0} is even". format(num))
# else:
#     print("{0} is odd". format(num))


#  print even or odd from the list
l = [1, 2, 3, 4, 5, 6, 7, 8]
even = []
odd = []
for i in l:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers are:", even)
print("odd numbers are:", odd)

# print leap year or not
# num = int(input("enter year:"))
# if (num%4==0 and num%100!=0) or (num%400==0):
#     print("leap year")
# else:
#     print("not a leap year")

l = [2021, 2022, 2023, 2024, 2025]
leap = []
notleap = []
for i in l:
    if (i%4==0 and i%100!=0) or (i%400==0):
        leap.append(i)
    else:
        notleap.append(i)
print("leap year:", leap)
print("not leap year:", notleap)

#  biggest value in the list
l = [-2, 2, 55, 33]
l1 = l[0]
l2 = l[0]
for i in l:
    if i>l1:
        l1 = i
    elif i<l2:
        l2 = i
print("biggest value is:", l1)
print("smallest value is:", l2)

# separate zeroes and ones from the list

l = [0, 1, 0, 1, 0, 1, 1, 0]
zeros = []
ones = []
for i in l:
    if i==1:
        ones.append(i)
    elif i==0:
        zeros.append(i)
    else:
        print("nothing")
print("ones are:", ones)
print("zeros are:", zeros)


# print unique values from the list

l = [1, 0, 1, 0]
values = set()
list = []
for i in l:
    if i not in values:
        values.add(i)
        values.add(i)
        list.append(i)
print("unique values are:", list)



# print prime numbers
def is_prime(numbers):
    if numbers>1:
        for num in range(2, numbers):
            if numbers%num==0:
                return "not a prime number"
        return "is a prime number"
    return " not a prime"
print(is_prime(9))


# take a list and print ascending order and descending order.

l = [5, 2, 9, 1, 7, 3]

asc = sorted(l)
print("Ascending Order:", asc)

desc = sorted(l, reverse=True)
print("Descending Order:", desc)


# Another way using for loop

l = [5, 2, 9, 1, 7, 3]

for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] > l[j]:
            l[i], l[j] = l[j], l[i]

print("Ascending Order:", l)


for i in range(len(l)):
    for j in range(i + 1, len(l)):
        if l[i] < l[j]:
            l[i], l[j] = l[j], l[i]

print("Descending Order:", l)



