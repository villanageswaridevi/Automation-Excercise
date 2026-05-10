"""
sequence[start:stop:step]
start – starting index (inclusive), defaults to 0
stop – ending index (exclusive), defaults to end of sequence
step – interval between elements, defaults to 1

"""
a = [1,2,3,4,5,6,7,8,9]

print(a[1:4])    # [2, 3, 4]
print(a[:3])     # first three: [1, 2, 3]
print(a[3:])     # from index 3 to end: [4, 5, 6, 7, 8, 9]

# Step and Skipping Elements
a = [1,2,3,4,5,6,7,8,9]
print(a[::2])     # every 2nd item: [1,3,5,7,9]
print(a[1:8:3])   # indices 1,4,7: [2,5,8]

# Negative Indices & Reverse
a = [1,2,3,4,5,6,7,8,9]
print(a[-2:])     # [8, 9]
print(a[:-3])     # all except last 3: [1,2,3,4,5,6]

a = [1,2,3,4,5,6,7,8,9]
print(a[::-1])    # reversed list [9,8,...,1]

# Works on Strings, Tuples, Other Sequences
s = "Hello, World!"
print(s[2:5])     # "llo"
print(s[-5:-2])   # substring near end
print(s[::-1])    # reversed string "!dlroW ,olleH"

# slice() Object for Reusability
sl = slice(1,4,2)
nums = [10,20,30,40,50]
print(nums[sl])        # [20, 40]
print("Python"[sl])    # "yh"

# Out‑of‑Bounds Slicing is Safe
print(a[7:15])    # [8, 9]
print(a[-15:])    # entire list

# Example Scenarios
fruits = ['apple','banana','cherry','date','fig','grape']

# first 3 fruits
print(fruits[:3])                 # ['apple','banana','cherry']

# fruits starting from index 2
print(fruits[2:])                 # ['cherry','date','fig','grape']

# every 2nd fruit
print(fruits[::2])                # ['apple','cherry','fig']

# last 3 fruits
print(fruits[-3:])                # ['date','fig','grape']

# reversed list
print(fruits[::-1])               # ['grape','fig','date','cherry','banana','apple']











