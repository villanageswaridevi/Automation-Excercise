"""
membership operators:
-->They are in, not in (True / False), to check the items presence in the sequence

"""

a = ["hate you", "miss you"]
print("love you" not in a) # returns True because a sequence with the value "love you" is not in the list
print("hate you" not in a) # returns false because a sequence with the value "hate you" is in the list

b = ["soaps", "shampoos"]
print("soaps" in b) # returns True because a sequence with the value "soaps" is in the list
print("facewash" in b) # returns False because a sequence with the value "facewash" is not in the list
