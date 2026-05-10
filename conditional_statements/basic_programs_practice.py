"""
take a list print even and odd
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
for i in l:
    if i%2==0:

        even.append(i)
    else:
        odd.append(i)
print("even numbers are:", even)
print("odd numbers are:", odd)


"""
print even or odd
"""
# numbers = int(input("enter the number:"))
# if numbers % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")

"""
take a list to print positive or negative integers
"""

l = [1, 2, 3, 4, 5, -1, -2, -3, -4]
positive = []
negative = []
for i in l:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
print("positive integers are:", positive)
print("negative integers are:", negative)

"""
check positive, negative or zero
"""
# num = int(input("enter a numbers:"))
# if num > 0:
#     print("is positive integer")
# elif num < 0:
#     print("is a negative integer")
# else:
#     print("zero")

"""
take a list print largest of two numbers
"""
l = [1, 43, 56, 34, 1, 10, 98]
a = l[1] # give index position from the list
b = l[2] # give index position from the list
if a > b:
    print("largest number is:", a)
else:
    print("largest number is:", b)

"""
check whether the number is in range or out of range
"""
l = [1, 2, 3, 4, 5, 6]
for i in l:
    if 1<=i<=5:
        print(i, "is range between 1 to 5")
    else:
        print(i, "out of range")


"""
check grade using list
"""
marks = [1, 30, 45, 2, 43, 50, 30, 100, 9]
names = ["nandhu", "shanu", "likitha", "esha", "bannu", "janu", "siva", "haseen", "lokesh"]

for mark, name in zip(marks, names):
    if mark >= 50:
        print(name, "got Grade A")
    elif mark >= 35:
        print(name, "got Grade B")
    elif mark >= 15:
        print(name, "got Grade C")
    else:
        print(name, "has Failed")

"""
check grade using dictionary
"""
marks = {"ishu":1, "haseen":30, "nandhu":45,
         "lokesh":2, "siva":43, "dhanu":50, "madhu":90, "vasavi":12, "sai":9}
for name, mark in marks.items():
    if mark >= 90:
        print(name, "got Grade A+ college topper")
    elif mark >= 50:
        print(name, "got Grade A")
    elif mark >= 35:
        print(name, "got Grade B")
    elif mark >= 15:
        print(name, "Got Grade c")
    else:
        print("failed")


"""
take a list to print max, min values 
"""

l = [1, 2, 3, 4, 5, 10, 12]
maximum = l[0]
minimum = l[0]
for i in l:
    if i > maximum:
        maximum = i

    elif i < minimum:
        minimum = i

print(maximum, "is a maximum value")
print(minimum, "is a minimum value")

"""
check whether leap year or not from the list
"""
l = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010]
for i in l:
    if i%4==0:
        print(i, "is leap year")
    else:
        print(i, "is not leap year")

name = "Nageswari"
vowels = "aeiou"
for ch in name:
    if ch in vowels:
        print(ch)


numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Prime numbers list:")

for num in numbers:
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num)

"""
Find the sum of numbers divisible by 3 and 4 between 1 and 100.
"""
total = 0

for i in range(1, 101):
    if i%3==0 and i%4==0:
        total += i
print("sum of numbers divisible by 3 and 5 between 1 and 100", total)

"""
Accept a number and print whether it is divisible by 5 and 11 or not
"""
l = [55, 110, 12, 13, 220]
for i in l:
    if i%5==0 and i%11==0:
        print(i, "divisible by both 5 and 11")
    else:
        print(i, "not divisible by both 5 and 11")


"""
Check whether a character is uppercase or lowercase in the list from the string
"""
list = "NagEswaRI"
uppercase = []
lowercase = []
for i in list:
    if i.isupper():
        uppercase.append(i)
        # print(i, "is uppercase")
    elif i.islower():
        lowercase.append(i)
        # print(i, "is lowercase")
print("uppercases are:", uppercase)
print("lowercases are:", lowercase)

"""
write a functions reverse a string without using inbuilt functions
"""

def reverse_str(s):
    tmp = ""
    for i in s:
        tmp = i + tmp
    return tmp

data = "nandha"
print(reverse_str(data))

"""
reverse string using inbuilt functions
"""

l = ["nandha"]
x = l[0][::-1]
print(x)

l = ["nandha", "naidu"]
l.reverse()
print(l)


s="nandhu"
temp=""
for i in s:
    temp = i + temp
print(temp)

"""
take a list to print zeros and ones separate
"""
l = [1, 0, 1, 0, 1, 0, 0]
zeros = []
ones = []
for i in l:
    if i == 0:
        zeros.append(i)
    elif i == 1:
        ones.append(i)
print("zeros are:", zeros)
print("ones are:", ones)


"""
take a list to print unique values like [0, 1]
"""
l = [1, 0, 1, 0, 1, 0, 0]
values = set()
list = []
for i in l:
    if i not in values:
        values.add(i)
        values.add(i)
        list.append(i)
print("unique values are:", list)

"""
take a list to print how many zeroes and ones in the list
"""
l = [1, 0, 1, 0, 0, 1, 1, 1]
for i in l:
    if i == 0:
        x = l.count(0)

    elif i == 1:
        y = l.count(1)
print("no.of zeroes are:",x)
print("no.of ones are:", y)

"""
fibonacci from the list
"""

l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Generate Fibonacci numbers up to max of the list
fib = [0, 1]
while True:
    next_num = fib[-1] + fib[-2]
    if next_num > max(l):
        break
    fib.append(next_num)

# Print Fibonacci numbers from the list using conditionals
for i in l:
    if i in fib:
        print(i, end=' ')


"""
find smallest and biggest number in the list
"""
l = [1, 2, 41, 29, 5, 16, 12]
biggest = l[0]
smallest = l[0]
for i in l:
    if i > biggest:
        biggest = i

    elif i < smallest:
        smallest = i

print("\nThe biggest value is:", biggest)
print("The smallest value:", smallest)

"""
Accept age and check if the person is eligible to vote.
"""

vote = {"nandha": 24, "haseen": 29, "siva": 15, "lokesh": 18}
for name, age in vote.items():
    if age >= 18:
        print(name, "eligible for vote")
    elif age <= 18:
        print(name, "not eligible for vote")


"""
Accept a password and check if it’s correct or not
"""
username = "Nageswari"
password = "nag@123"

user = input("enter username:")
if user == username:
    pas = input("enter password:")
    if pas == password:
        print("successfully logined")
    else:
        print("incorrect password, enter valid password")
else:
    print("invalid username")


"""
Print all even numbers from 1 to 50.
"""
for i in range(1, 51):
    if i%2==0:
        print(i, "is a even number")




















