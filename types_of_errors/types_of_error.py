"""

SyntaxError	-->  Wrong Python syntax	-->  if x = 5 instead of x == 5
IndentationError	--> Wrong or inconsistent indentation	--> Missing or extra tabs/spaces
NameError	--> Using variable/function before defining it	--> print(a) when a not defined
TypeError	--> Wrong type used in an operation	--> "5" + 2
ValueError	--> Right type, but wrong value	--> int("abc")
IndexError	--> List index out of range	--> list[5] when list has 3 items
KeyError	--> Accessing a dictionary key that doesn’t exist	--> my_dict["missing_key"]
AttributeError	--> Calling a method/attribute that doesn't exist	--> "abc".push()
ZeroDivisionError	--> Dividing a number by zero	--> 5 / 0
ImportError	--> Importing a module that doesn't exist	--> import numppy (typo)
ModuleNotFoundError	--> Similar to ImportError, module is not installed	--> import flask (if not installed)
FileNotFoundError	--> Trying to open a non-existing file	--> open("nofile.txt")
RecursionError	--> Too many recursive function calls	--> Function calls itself forever

"""
l = [1, 2, 3, 4, 5]
for i in l:
    if i >= 6:
        print(i)
    # else:
        # print("invalid data")

d = {"Andhra": "Amaravathi", "telangana": "Hyderabad", "Karnataka": "Bangaluru"}
print(d.keys())


