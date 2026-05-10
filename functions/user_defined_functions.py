"""
User defined functions: we can define by using def keyword

syntax: def function_name(args):
        function body

purpose: we can reuse the code, maintenance is easy
"""
# 1.positional argument
# 2.default argument
# 3.variable length arguments
# 4.keyword argument
# 5.keyword length argument

# Example :
def function_name(): # function definition
    print("hate you") # function body
#     we can use if, for, while, operators anything we can
function_name() # function calling

def fun(name, place):
    print("my name is {}".format(name))
    print("my home town is {}".format(place))
    fun("nandha", "yanam")


def fun1(name, course, place = "Sunkatarevu"):
    print("Name:{}".format(name))
    print("Place:{}".format(place))
    print("course:{}".format(course))

fun1("Nandha", "Python", "Sunkatarevu")


# keyword arguments:
def fun2(name, place):
    print(name)
    print(place)

fun2("Nageswari", "Yanam")

# **v.v.imp: variable length arguments:

# def fun(*args, **kwargs)

def fun(*args):
    print("args", args)

fun(1, 2, 3, 4)

def family_members_fun(*nandhu): # we can provide any args as names
    print("args", nandhu)
    for i in nandhu:
        print(i)

family_members_fun("Anandarao", "Amaravathi", "Veeraveni", "Nageswari")

def details_fun(**kwargs):
    print(kwargs)

details_fun(name = "Nandhu", age = 24)

def final_fun(name, place = "yanam", *args, **kwargs):
    print("Name:", name)
    print("place:", place)
    print(args)
    print(kwargs)
final_fun(name="Nandha", place="yanam", course="python")




# function is a block of code, it is dedicated to perform some task
# inbuilt functions
# user defined functions
# special functions




















