# re: regular expressions is used for to find the pattern string

import re

# match : It will look for begining of the string, if pattern matches in the string
# then only it will return match object
# search : it will check from begining of the string, once it will search pattern it will object
# findall : it will return all the matched items in the list
# compile : we can use with pattern and it can be used with other methods like method,search etc..
# sub : substitute string with pattern in all the occurences
# subn : it will replace / substitute only n of occurences based on the n counter
# r means raw string

# a = "Hello World, I am learning python. I am average at python"
# b = "python is very easy to learn"
# print(re.search(r'python', a)) #It searches for a pattern in a string.
# If the pattern is found anywhere, it returns a match object; otherwise, it returns None.
# print(re.search(r'python', a).group()) #It returns the exact part of the string where the pattern matched.
# print(re.match(r'python', b).group()) # It checks if the pattern matches at the beginning of the string.
# print(re.findall(r'python', a)) #It is used to find all matches of a pattern in a given string.
# print(re.sub(r'python', 'PYTHON', a)) # used to replace parts of a string that match
# a regular expression pattern.
# print(a)
# print(re.subn(r'python', 'Python', a, count=1)) # Substitutes all (or limited number of)
# matches of a pattern in a string with a replacement, and also returns how many substitutions were made.

# obj = re.compile(r'python', re.IGNORECASE) # we can use with pattern and it can be used with other methods like method,search etc..
# print(re.search(obj, a).group())
# print(re.match(obj, b).group())
# print(dir(re))
# print(re.search(obj, a).group()) # to perform case-insensitive matching.


# pattern sysntax:
"""
\w : it will match only single char
\w+ : it will match only chars except new line
\d : it will print only digit
\d+ : it will print only digits except new line, any space or any (.)point it won't print
\W : non char values
\D : non digit
\s : white space \ tab space 
^ : it will be string stars
$ : it will be string ends
. : any single char except line
* : zero re more repeaters
+ : one or more
? : zero or one
{n} : n times repeaters
[abc] : a, b, c
[a-zA-Z0-9] :
() : 


"""
# example

a = "hello world, I am using python 3.14 version"
print(re.search(r'\w', a).group()) # it will returns first letter of the string "h"
print(re.search(r'\w+', a).group()) # it will returns first word of string except new line hello
print(re.search(r'\d', a).group()) # it will returns first digit 3
print(re.search(r'\d+', a).group()) # it will returns first digit except new line 3
print(re.search(r'\d.', a).group()) # it will returns first digit with . (dot) 3.
print(re.search(r'\d.*', a).group()) # it will returns 3.14 version
print(re.search(r'\w.*', a).group()) # it will returns entire string hello world, I am using python 3.14 version
print(re.search(r'hello?',  'hell').group()) # it will only matches items what we are given hell
print(re.search(r'l{2}', 'hello python 314 hello python 312').group()) # it will returns how
# many times char will be repeat
print(re.search(r'\d{3}', 'hello python 314 hello python 312').group()) # it will returns no.of digits 314
print(re.search(r'\d+\s[a-z]', 'hello python 314 hello python 312').group())
# it will returns after digit char 314 h
print(re.search(r'\d+\s[a-z]+', 'hello python 314 hello python 312').group())
#  it will returns after digit word 314 hello
print(re.search(r'[a-z0-9A-z\s]+', 'hello python 314 hello python 312 learning.').group())
# it will returns entire string what we given hello python 314 hello python 312 inside the square
# brakets what are the words to match . (dot) not print because we are not given if we given in end of the
# pattern provide then only print
print(re.search(r'[a-z0-9A-z.@\s]+', 'hello python 314. @ welcome to python chanel').group())
# it will re returns entire string with special chars also because we are providing in the
# pattern hello python 314. @ welcome to python chanel
print(re.search(r'\w+@gmail.com', 'nandha123@gmail.com').group())
# it will returns the all values with special cases also
print(re.search(r'[\w].+@gmail.com', 'nandha.123@gmail.com').group())
# it will return all the string with spaces and new lines also
print(re.search(r'[\w].+[@gmail|yahoo|email.com]', 'nandha.123@email.com').group())
# it will returns anything we provide because we are providing or [|] operator
print(re.search(r'[a-z0-9.]+@(gmail|email)\.com', 'nandha.123@gmail.com').group())
# another way to print all the string

import re

text = ''' IPv6 Address. . . . . . . . . . . : 2406:7400:61:b81b::1007
   Link-local IPv6 Address . . . . . : fe80::e72d:838b:720e:656b%13
   IPv4 Address. . . . . . . . . . . : 192.168.68.110
   Subnet Mask . . . . . . . . . . . : 255.255.255.0
   Default Gateway . . . . . . . . . : fe80::8e90:2dff:fec7:a020%13
                                       192.168.68.1 
'''

pattern = r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b' # # Regular expression pattern for matching IP addresses

ip_addresses = re.findall(pattern, text) # # Find all IP addresses in the text

for ip in ip_addresses:
    print(ip)
































