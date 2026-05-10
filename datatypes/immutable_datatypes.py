"""
Data types:
int – Whole numbers
 Example: 10, -3

float – Decimal numbers
 Example: 3.14, 0.5

str – Text (called string)
 Example: "Hello", 'Python'

bool – True or False values
 Example: True, False


tuple – Collection of items, unchangeable
 Example: (1, 2, "Nandhu")


Immutable data types: Int, str, tuple --> we cannot change, once we defined we cannot able to modify
throught the program execution.


"""

# Int example :
#     age = 24
#     amount = 100
#     amount = 100.50 # this is a float value also used in integers
#     door_no = 2-10
#     flat = 916

# str example : string must be in double quotes only.
# name = "Nandhu"
# place = 'Banglore'
# address = """Banglore @ Marthahalli"""

# tuple example: tuple can closed wih brackets() inside that hetrogeneous values it can allow integers,strings,
# it can allow anything.

# t = (2, "name", 1, 4, 3)

"""
inbuilt methods: while installing the python we will get all this methods
 sum, min, max
**id, type, help, dir

function is a block of code, it will do some certain action

"""
age = 10
print(age)
print(id(age))
print(type(age))
# print(help(age))
# print(help(str))

print(dir(age))
print(age.bit_count())
print(age.bit_length())
print(age.conjugate())
print(age.as_integer_ratio())

# magic methods or dunder methods

# Integer: int is a immutable datatype we cannot able to modify entire program execution.
a = 5
print(id(a))
a = 10
print(id(a))

# string
name = "nandhu naidu"
print(dir(name))
print(name.capitalize()) # capitalize method is to print the first letter in uppercase
print(name.casefold()) # case fold method is used to print all letters in lowercase
print(name.center(50))
"""
center method is used to center-align a string within a 
specified total width, optionally filling the extra space with a custom character (defaults to a space). 
It returns a new string and leaves the original unchanged.
"""
print(name.title()) # title method is used to print the first letter will be capital in each word
print(name.swapcase())
"""
this method is used to swap the values like lowercase converted into 
uppercase and uppercase converted into lowercase.

"""
print(name)
print(name.find("d")) # it will return the index position, the index will start from 0,1,2... so the output is 3
print(name.index("a")) # it will also same as find method
print(name.count("n")) # it will return no.of occurences

"""
count method is used to count the no.of letters what we are given in the word.
And this method is available in all datatypes. what are the seq we have, seq means no.of items like str,list,tuple
have the count method.
"""
print(name.split(" ")) #it will return list of words

mn = " nandha "

print(mn.strip(" ")) # it will fix the edges like we any spaces are there in string it will remove the spaces
print(mn.lstrip(" ")) # it will remove the left side space
print(mn.rstrip(" ")) # it will remove the right side space
print(mn.upper()) # it will converted all letters into uppercase
print(mn.lower()) # it will converted all letters in lowercase
print(mn.islower()) # boolean value, true
print(mn.isupper()) # boolean value, false
print(mn.isdigit()) # boolean value, false
print(mn.isalnum()) # boolean value, false
print(mn.isalpha()) # boolean value, false
print(mn.isdecimal()) # boolean value, false
print(mn.isidentifier()) # boolean value, false
print(mn.isnumeric()) # boolean value,false
print(mn.isprintable()) # boolean value, true
print(mn.isspace()) # boolean value, false
print(mn.istitle()) # boolean value, false
print(mn.startswith("n")) # false because it will start with space
print(mn.endswith(" ")) # true because it will ends with space
print(mn.encode()) # it will returns an encoded version of the string

text = "Hello\tWorld"
print(text.expandtabs(10)) # sets the tab size of the string

value =  "Hi {} how are you {}"
print(value.format("ji", "Are you ok")) # formats specified values in a string


fullname = ["villa", "Nageswari", "devi"]
print(" ".join(fullname)) # it is used to join the all words

main = "Nandhu"
print(main.zfill(10)) # it will return to fill the string with a specified no.of 0 values at the beginning

word = "villa nageswari devi"
print(word.removeprefix("villa")) # means starting word it will return remaining words what we are given.
print(word.removesuffix("devi")) # means end word it will return remaining words what we are given.
print(word.replace("villa nageswari devi", "nandha naidu villa")) # it will be replace with
# new words what we are print.


# Tuple: is a data type, it is immutable data type, we can define by using (), it can have any values.
t = (1 ,2, 3, 2, 4, 5)
print(type(t))
print(dir(t))
print(t.count(2)) # it will return no.of occurences
print(t.index(4))
print(t.index(4))

l = "Nageswari"

# Unique characters preserving order
unique = []
for c in l:
    if l.count(c) == 1 and c not in unique:
        unique.append(c)

# Repeated characters
repeated = []
for c in set(l):
    if l.count(c) > 1:
        repeated.append(c)

print("Repeated:", repeated)
print("Unique:", unique)



int = 1
print(int)

