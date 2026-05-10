# take a list and print composite numbers

numbers = [2, 4, 7, 9, 13, 15, 17, 20, 1]

for num in numbers:
    if num > 1:
        is_composite = False
        for i in range(2, num):
            if num % i == 0:
                is_composite = True
                break
        if is_composite:
            print(num, "is a Composite Number")
    else:
        continue


#  take a list and print Armstrong Number
numbers = [153, 370, 371, 9474, 143, 10, 407]

for num in numbers:
    original = num
    sum_of_powers = 0
    digits = str(num)
    power = len(digits)

    for digit in digits:
        sum_of_powers += int(digit) ** power

    if sum_of_powers == original:
        print(original, "is an Armstrong number")
    else:
        print(original, "is not an Armstrong number")

#  take a list and print Disarium Number
numbers = [89, 135, 175, 518, 123, 10, 12]

for num in numbers:
    original = num
    digits = str(num)
    total = 0

    for i in range(len(digits)):
        total += int(digits[i]) ** (i + 1)  # position starts from 1

    if total == original:
        print(original, "is a Disarium Number")
    else:
        print(original, "is NOT a Disarium Number")


#  take a list and print spy numbers
# sp means sum of digits equal to product of the numbers
numbers = [123, 1124, 22, 141, 132]

for num in numbers:
    digits = [int(d) for d in str(num)]
    digit_sum = sum(digits)
    digit_product = 1
    for d in digits:
        digit_product *= d
    if digit_sum == digit_product:
        print(num, "is a SPY Number")
    else:
        print(num, "is NOT a SPY Number")









#  l = [1, 2, 3, 4, 5, 6, 7, 8]
#
#  I want output = [1, 6, 11, 16]
#
#  without using reduce and inbuilt functions
#
l = [1, 2, 3, 4, 5, 6, 7, 8]

output = []
i = 0
while i < len(l):
    if i == 0:
        output.append(l[i])  # First element
    elif i + 1 < len(l):
        output.append(l[i] + l[i+1])
        i += 1  # skip next element (already used)
    i += 1

print(output)

