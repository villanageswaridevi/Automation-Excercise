"""
take a list to print positive and negative integers
"""
l = [1, 2, 3, -11, -22, -33]
positive = []
negative = []
for i in l:
    if i > 0:
        positive.append(i)
    elif i < 0:
        negative.append(i)
    else:
        print("zero")
print("positive integers:", positive)
print("negative integers:", negative)

"""
write a program positive and negative integers without using list
"""
l = int(input("enter integer:"))
if l > 0:
    print("positive integer")
elif l <0:
    print("negative integer")