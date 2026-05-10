"""
take a list to print zeros and ones seperatly
"""
l = [1, 0, 1, 0, 0, 1, 0]
zeros = []
ones = []

for i in l:
    if i == 0:
        zeros.append(i)
    elif i == 1:
        ones.append(i)

print("zeros:", zeros)
print("ones:", ones)

"""
take a list and print the unique values like [0,1]
"""
l = [1, 0, 1, 0, 1, 0, 1]
values = set()
list = []

for i in l:
    if i not in values:
        values.add(i)
        values.add(i)
        list.append(i)
print("unique values:", list)

"""
take a list and print how many zeros and ones
"""
l = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
for i in l:
    if i == 0:
        x = l.count(0)
    elif i == 1:
        y = l.count(1)
print("no.of zeros:", x)
print("no.of ones:", y)




