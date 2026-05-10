"""
adding arguments
"""
def funtion(name, cource):
    print("my name is {}".format(name))
    print("my cource is {}".format(cource))
funtion("nandhu", "python")

"""
adding missing arguments
"""
def fun1(name, cource, place = "bengalore"):
    print("my name is {}".format(name))
    print("my cource is {}".format(cource))
    print("Im in {}".format(place))
fun1("nandhu", "python", "bengalore")

"""
take a string and reverse the string without using inbuilt
"""
def reverse_str(s):
    tmp = ""
    for i in s:
        tmp = i + tmp
    return tmp
data = "nandha"
print(reverse_str(data))

"""
print weeks names what we are given data thats only print
"""
def weeks(w):
    if w == 1:
        print("monday")
    elif w == 2:
        print("tuesday")
    elif w == 3:
        print("wednesday")
    elif w == 4:
        print("thursday")
    elif w == 5:
        print("friday")
    elif w == 6:
        print("saturday")
    else:
        print("invalid")

data = 1
weeks(data)

"""
print zeroes and ones
"""
def zeros_ones(z):
    zeroes = []
    ones = []
    for i in z:
        if i == 0:
            zeroes.append(i)

        elif i == 1:
            ones.append(i)
    print("zeroes are:", zeroes)
    print("ones are:", ones)
data = [1, 0, 1, 0, 0]
zeros_ones(data)

"""
write a program to print how many zeroes and ones in the list
"""
def no_zeros_ones(n):
    zeros = []
    ones = []
    for i in n:
        if i == 0:
            # zeros.count(0)
            zeros.append(i)
        elif i == 1:
            # ones.count(1)
            ones.append(i)
    print("no.of zeros:", len(zeros))
    print("no.of ones:", len(ones))
data = [1, 0, 1, 0, 1, 1, 0]
no_zeros_ones(data)


"""
write a program to print fibonacci series
"""
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
fibonacci(10)





"""
find smallest and biggest number in the list
"""
def small_bigg(s):
    biggest = float('-inf')
    smallest = float('inf')

    for i in s:
        if i > biggest:
            biggest = i
        if i < smallest:
            smallest = i

    print("\nBiggest value is:", biggest)
    print("Smallest value is:", smallest)

data = [1, 31, 22, 41, 21]
small_bigg(data)

def even(n):
    even = []
    odd = []
    for i in n:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    print("even numbers are:", even)
    print("odd numbers are:", odd)
data = [156, 225, 223, 228]
even(data)

"""
Accept age and check if the person is eligible to vote.
"""
def vote(v):
    for name, age in v.items():
        if age >= 18:
            print(name, "is eligible for vote")
        elif age <= 18:
            print(name, "is not eligible for vote")
list = {"nandha": 10, "haseen": 16, "suresh": 34, "madhu": 30}
vote(list)


# Positional Arguments:
def great(name, age):
    print(f"Name: {name} \nAge: {age}")
great("Nandha", 25)

#  Default Arguments:
def details(name = "Nandha"):
    print(f"Hello {name}")
details()
details("Nandhu")

# key word argument
# def arg(Name, Age):
#     print(f"Name: {Name}, Age: {Age}")
# arg(Name = "Nandha", Age = 25)

# Variable length argument
def total(*num):
    print(sum(num))
total(1, 2, 3, 4, 5)

# **kwargs
def details(**info):
    print(info)
details(name = "Nandha", age = 25)

























