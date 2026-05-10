"""
Looping statements:
for loop, while loop,
"""

# For loop: A for loop in Python is used to repeat a block of code for each item in a sequence
# syntax: for var in sequence:


# to check even numbers in for loop

a = [1, 2, 3, 4, 5, 6, 7, 8]
l = []
for i in a:
    if i%2==0:
        l.append(i)
        # print("{} is even number". format(i))
print(l)


# To check odd numbers in for loop
b = [1, 2, 3, 4, 5, 6, 7, 8]
l = []
for i in b:
    if i%2!=0:
        l.append(i)
        # print("{} is odd number". format(i))
print(l)

x = "hate you"
# vowels = "aeiou"
l = []
for i in x:
    if i in "aeiou":
        l.append(i)
print(l)

y = "miss you"
l = []
for i in y:
    if i == "a" or i =="e" or i == "i" or i=="o" or i=="u":
        l.append(i)
print(l)


a = "hello world"
b = "python program learning"
l = []
for i in a:
    if i in b and b.count(i)>1:
        print(i)
        l.append(i)
print(l)

# another way:
a = "hello world"
b = "python program learning"
l = []
for i in a:
    if i in b:
        if b.count(i)>1:
            print(i)
            l.append(i)
print(l)

d = {"a":1, "b":2, "c":3, "d":4}
for k,v in d.items():
    if v%2==0:
        print(v)

d = {"a":1, "b":2, "c":3, "d":4}
for k,v in d.items():
    if v%2==0:
        print(v)

        for k, v in d.items():
            if v % 2 != 0:
                print(k, v)


# while loop: repeatedly executes a block of code **as long as a condition is true
# syntax: while condition:
           # code



# Example:
i = 1
while i<5:
    print("i:{}".format(i))
    i+=1


# Conditional statements: break, continue, pass

# break statement: this statement can stop the loop even if the while condition is true

a = [1, 2, 3, 4]
for i in a:
    print(i)
    if i == 3:
        break  # once break statement is executed, after that it won't execute any line
        print("after break ststement")


i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# continue statement: this statement can stop the current iteration, and continue with the next
a = [1, 2, 3, 4, 5]
for i in a:
    if i == 3:
        continue
        print("after continue")
    print(i)

i = 0
while i<6:
    i+=1
    if i==3:
        continue
    print(i)


# pass statement:
# The pass statement in Python is a placeholder that does nothing.
# It is used when a statement is required syntactically, but you don’t want to write any code there yet.

# Example:

i = 0
while i<6:
    pass # if we are not using this statement the error will be raised

l = [1, 2, 3, 4, 5, 6]






































