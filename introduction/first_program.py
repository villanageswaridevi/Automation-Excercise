"""
This file is contains python training cource
"""
print("Hate you")

"""
what is python?
Python is a simple, easy-to-learn programming language used to create software, websites,
apps, and automate tasks.

characteristics of Python:
1. easy to learn and readable
2. dynamically typed language
3. interpreted language
4. object - oriented language
5. high level language

 
whare we can use?
server - client communication programming
web application development - Django, flask etc..
python can be used in Data science / AI&ML - pandas, numpy, scipy
where we can use:  network applications, gaming apps, webScrapy
Main agenda: Software application automation testing - selenium webdriver, requests, os, paramiko

"""

"""
1.Indentation: function,classes, loops etc  having indented blocks.
Naming conventions: classes,functions, data types.
comments: 1.single line 2. multi line 
"""

# <-- This is single line comment. And this is an example for single line comment.
"""
<-- This is multi line comment. We can write multiline comments.
This is an example for multiline comments.
comments can be use in class docs, function docs and file docs.
"""

class Fun:
    """
    This is class docs string
    this is example for comments
    """
    def fun(self):
        """
        this function contains hello world
        :return:
        """
        print("hello world")
        def fun2(self):
            print("hello")
            print("fun2")
#             fun2 sum of two numbers
#               print(2+1)

# Naming conventions:
# valid:
name = "Nandhu"
_name = "Nandhu"
__name = "Nandhu"
first_name = "Nandhu"
Name1 = "Nandhu"

# Class name must be Capital
# what is class? : A class defines a set of attributes (variables)
# and methods (functions) that describe the behavior and state of an object.
# variable names should be lowercase / camelcase

# Invalid:
"""
1name = "Nandhu"  # cannot sart with intergers, or any special charectors, space is also don't allow
@name = "Nandhu"
  name = "Nandhu"
"""