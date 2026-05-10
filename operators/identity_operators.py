"""
Identity operators

-->Identity operators are used to compare the objects,
 not if they are equal, but if they are actually the same object, with the same memory location
 -->They are is, is not, (True / Fase), it will check the objects
"""

x = ["hate you", "miss you"]
y = ["hate you", "miss you"]
z = x
print(x is z) # returns True if both variables are the same object
# returns True because z is the same object as x
print(x is y) # returns False because x is not the same object as y, even if they have the same content
print(x == y) # to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
# Returns True if both variables are not the same object
print(x is not y)
print(x is not z)











