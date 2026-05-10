# list comprehensions:
# dict comprehensions:


# l = [return_val for i in seq]
# l = [return_val for i in seq if condition]

l = [1, 2, 3, 4, 5, 6, 7, 8]
l1 = [2, 4, 6, 8]

l2 = [i*i for i in l]
l3 = [i+i for i in l]
l4 = [i for i in l if i%2==0]


print(l2)
print(l3)
print(l4)

a = "hello world"
s1 = [i for i in a if i in "aeiou"]
print("".join(s1))



l = [[1, 2], [3, 4], [5, 6]]
l1 = [j for i in l for j in i if j%2==0]
print(l1)


s = "msn python youtube channel"

l1 = list(set([(i, s.count(i)) for i in s]))
print(l1)

l2 = [i.capitalize() for i in s.split(" ")]
l3 = [i[0].upper()+i[1:] for i in s.split(" ")]

print(l2)
print(l3)



# d = {exp for i in seq}
s = "msn python youtube channel python channel"
# d = {"key1": "value1", "key2":"value2"}
d1 = {i:s.count(i) for i in s}
d2 = {i:s.count(i) for i in s if i in "aeiou"}
d3 = {i:s.count(i) for i in s if s.count(i)>1}
d4 = {i:s.count(i) for i in s.split(" ")}

print(d1)
print(d2)
print(d3)
print(d4)















