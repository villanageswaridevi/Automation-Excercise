"""
conditions: if, else, elif
Conditional statements: break, continue, pass

"""
# if statement :This condition is something if it is satisfied it will perform some actions.
# if we have only one condition we can use if statement
#  syntax: if condition:
# Body of the condition / code

a = 10
b = 20
if a<b:
    print("a is less than b")

x = 10
y = 10
if x==y:
    print("x is equals to y")

c = 2
d = 1
if c>d:
    print("c is greater than d")

c = 1
d = 2
if c!=d:
    print("c is not euals to d")

x = 10
y = 20
if x<=y:
    print("x is less than or equals to y")

x = 10
y = 20
if x>=y:
    print("x is greater than or equals to y") # it will not print because it's false

# else statement:This condition we can use only one or to conditions.
# syntax: if condition:
#         else:

a = 10
b = 20
if a>b:
    print("a is greater than b")
else:
    print("a is not grater then b") # this condition can use end of the code



# elif statement:This condition we can use multiple conditions.
# syntax: if condition:
#         elif condition:
#         elif condition:

x = 1
y = 2
z = 3
if x==y:
    print("x is euals to y")
elif x>y:
    print("x is greater than y")
elif x<y:
    print("x is less than y")
elif x>z:
    print("x is greater than z")
elif z!=y:
    print("z is not equals to y")
else:
    print("none of the above conditions are satisfied")

# nested condition:You can have if statements inside if statements, this is called nested if statements.
a = 40
if a>10:
    print("above 10")
    if a==40:
        print("equal to 40")
        if a!=10:
            print("not equal to 10")
        else:
            print("not above 20")
























