"""
take a list to print biggest value
"""
from sys import float_info

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
biggest = l[0]
for i in l:
    if i > biggest:
        biggest = i
print("biggest value is:", biggest)

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
smallest = l[0]
for i in l:
    if i < smallest:
        smallest = i
print("smallest value is:", smallest)




"""
take a list to print second biggest value
"""
l = [1, 2, 4, 36, 21]
first = second = float("-inf")
for i in l:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i
        print("second biggest value is:", second)

"""
take list to print third biggest value
"""


a = [1, 2, 3, 4, 20, 30]
first = second = third = float("-inf")

for i in a:
    if i > first:
        third = second
        second = first
        first = i
    elif i > second and i != first:
        third = second
        second = i
    elif i > third and i != second and i != first:
        third = i

print("third biggest value is:", third)













