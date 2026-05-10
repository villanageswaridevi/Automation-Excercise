"""
exception handling:
error: syntax error
exception: we can handle those exception by using some keywords
keywords: try, except, else, finally
raise: custom exception by using raise

syntax:
try:
# code
# we can write code, main logic
except:
# code
# we can handle exception here
else:
# code
finally
# code
"""
from conditional_statements.basic_programs_practice import negative


def exception_handling(a,b):
    try:
        c=a/b
        print(c)
    except ZeroDivisionError as e:
        print("got exception", e)
    except ValueError as e:
        print("value error", e)
    except KeyError as e:
        print("kay error", e)
    else:
        print("executed else block")
    finally:
        print("executed every time")

exception_handling(10, 0)




# try:
#     for i in range(1, 11):
#         if i%2==0:
#             print(i)
# except:
#     print("got exception")



# try:
#     limit = int(input("enter value:"))
#     print("even numbers are:")
#     for i in range(limit + 1):
#         if i%2==0:
#             print(i)
# except:
#     print("nothig")

# raise: custom exception by using raise keyword


# Step 1: Define custom exception
class NegativeNumError(Exception):
    pass

# Step 2: Define a function
def fun(a):
    if a < 0:
        raise NegativeNumError("Error: Negative number")
    else:
        print("Value is valid:", a)


# Step 3: Use try-except to handle the exception
try:
    fun(-2)
except NegativeNumError as e:
    print(e)


class PositiveNumError(Exception):
    pass

def fun(b):
    if b>=0:
        raise PositiveNumError("Positive")
    else:
        print("Negative number", b)

try:
    fun(-2)
except PositiveNumError as e:
    print(e)


"""
First create a function
use exception handling mechanism
"""
# find the given number is even or odd
def is_even_odd(n):
    try:
        if n % 2 == 0:
            return "Even"
        else:
            return "Odd"
    except ValueError as e:
        print("Got Exception:", e)
    except TypeError as e:
        print("Type Error:", e)
        return "Invalid Data"

print(is_even_odd(2))  # Output: Even












