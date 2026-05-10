# Mutable data types: list, dict, set

"""
list:
-->It is mutable datatype, it is define by using [], it can have any items as values.
It will support all the operations like adding, remove and update the values
-->Collection of items, changeable

Example: [1, 2, "Nandhu"]
"""
l = [1, 2, 3, "Nandhu"]
# print(type(l))
print(dir(l))
# 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'
l.insert(3,"nanna")  # add an element at the specified position
print(l)
l[4] = "MN" # it will return to modify
print(l)

fruits = ["Papaya", "Pipeapple", "Kiwi"]
fruits.append("Orange") # adds an element at the end of the list
print(fruits)

x = fruits.count("Papaya") # Returns the number of elements with the specified value
print(x)
fruits.clear() # Removes all the elements from the list
print(fruits)

fruits1 = ["apple", "banana", "cherry"] # Returns a copy of the list
x = fruits1.copy()
print(x)

soaps = ["Santoor", "Mysore", "Lux"]
shampoos = ["Dove", "Clinicplus", ]
soaps.extend(shampoos) # add the elements of a list to the end of the current list
print(soaps)

x = soaps.index("Lux") #it will return the index of the first element with the specified value
print(x)

soaps = ["Santoor", "Mysore", "Lux"]
soaps.pop(1) # removes the element at the specified position
print(soaps)
soaps = ["Santoor", "Mysore", "Lux"]
soaps.remove("Lux")# removes the first item with the specified value
print(soaps)
soaps = ["Santoor", "Mysore", "Lux"]
soaps.reverse()# reverses the order of the list
print(soaps)
lollypops = ["White", "Black", "Pink"]
lollypops.sort() # sort the list alphabetically
print(lollypops)



"""
dict:
-->It is an mutable datatype and we can define by using {} 
-->dict can contain key and value pairs, it is having , (coma) separated the values
–-> Key-value pairs
-->key should be unique, it won't allow duplicate keys but values can anything 
-->key should be immutable datatype, int, str, tuple
Example: {"name": "Nandhu", "age": 25}
"""
# d = {"name": "Nandha"}
# print(type(d))
# print(dir(d))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values'
info = {"name": "Nandha", "age": 25, "gender":"female", "height": 5.6}
info.clear() # it will removes all the elements from the dictionary
print(info)

details = {"name": "Nandha", "age": 25, "gender":"female", "height": 5.6}
details.copy()
print(details)

a = ("key1", "key2", "key3")
b = 0
x = dict.fromkeys(a, b) # it will returns the dictionary with the specified keys and value
print(x)

info1 = {"name": "Nandha", "age": 25, "gender":"female", "company":"TAO Digitals"}
x = info1.get("company") # it will returns the value of the specified key
print(x)

personal = {"name": "Nandha", "age": 25, "gender":"female", "DOB":"25/08/2001",
            "company":"TAO Digitals", "salary": 10000}
x = personal.items()  # returns a list containing a tuple for each key value pair
print(x)

personal = {"name": "Nandha", "age": 25, "gender":"female", "DOB":"25/08/2001",
            "company":"TAO Digitals", "salary": 10000}
personal.pop("company") # it will removes the element with the specified key
print(personal)

personal = {"name": "Nandha", "age": 25, "gender":"female", "DOB":"25/08/2001",
            "company":"TAO Digitals"}
personal.popitem() # remove the last item from the dictionary
print(personal)

personal = {"name": "Nandha", "age": 25, "gender":"female", "DOB":"25/08/2001",
            "company":"TAO Digitals"}
personal.update({"aadhar number":"123456"}) # updates the dictionary with the specified key-value pairs
print(personal)

personal = {"name": "Nandha", "age": 25, "gender":"female", "DOB":"25/08/2001",
            "company":"TAO Digitals"}
x = personal.values() # returns a list of all the values in the dictionary
print(x)


"""
set – 
-->It is a mutable datatype, and it is define by using {}, with ,(coma) separated values.
-->it won't duplicate
-->Unordered collection of unique items

Example: {1, 2, 3}
"""

set = {"hate you", "missing you"}
# print(type(set))
# print(dir(set))
# 'add', 'clear', 'copy', 'difference', 'difference_update', 'discard', 'intersection', 'intersection_update',
# 'isdisjoint', 'issubset', 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update',
# 'union', 'update'
set.add("love you") # add am element to the set
print(set)

set = {"hate you", "missing you"}
set.clear() # it will remove all elements from the set
print(set)

set = {"hate you", "missing you"}
set.copy() # it will returns a copy of set
print(set)


x = {"sing", "cric", "alcho"}
y = {"valley", "sing", "choco"}

z = x.difference(y) # returns a set containing the difference between two or more sets
a = y.difference(x)
print(z)
print(a)

x = {"sing", "cric", "alcho"}
y = {"valley", "sing", "choco"}
z = x.intersection(y) # returns a set, that is the intersection of two other sets
print(z)

set = {"hate you", "missing you", "love you"}
set.discard("missing you") # it will remove the particular value from the list
print(set)

x = {"sing", "cric", "alcho"}
y = {"valley", "dance", "choco"}
z = x.isdisjoint(y) # it will returns whether two sets have a intersection or not
print(z)

x = {"sing", "cric", "alcho"}
y = {"valley", "dance", "choco", "sing", "cric", "alcho"}
z = x.issubset(y) # it will returns whether another set contains this set or not
a = y.issubset(x)
print(z)
print(a)

x = {"sing", "cric", "alcho"}
y = {"valley", "dance", "choco", "sing", "cric", "alcho"}
a = x.issuperset(y)
z = y.issuperset(x) # returns whether this set contains another set or not
print(a)
print(z)

set = {"hate you", "missing you", "love you"}
set.pop() # removes an element from the set
print(set)

set = {"hate you", "missing you", "love you"}
set.remove("love you") # Removes the specified element
print(set)

x = {"sing", "cric", "alcho"}
y = {"valley", "sing", "choco"}
z = x.union(y) # return a set containing the union of sets
print(z)

x = {"sing", "cric", "alcho"}
y = {"valley", "sing", "choco"}
x.update(y) # update the set with the union of this set and others
print(x)


















