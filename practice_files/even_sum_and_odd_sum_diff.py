"""
take a list sum of even numbers and odd numbers and total difference b/w even and odd numbers
"""

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = 0
odd_sum = 0
for i in l:
    if i%2==0:
        print(i)
        even_sum += i
    else:
        print(i)
        odd_sum += i
print("sum of even numbers:", even_sum)
print("sum of odd numbers:", odd_sum)
print(even_sum - odd_sum)


