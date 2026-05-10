# open () by using open method we can perform file operations
# with open() by using this method we can perform file operations
"""
file modes:
w: write mode --> if file is not there it will create the file and write the data, if already file exists it will
 override the data
r: read mode --> if file exists it will read the data otherwise it will through exception
a: append mode --> it will append the data at end of the file
w+: write and read: if file is not there it will create the file, if file is there
it will override data and we can read the data from the file
r+: read and write: we can read and write but we cannot create new file not exist
a+: we can read, write and create a new file if file not exists

wb:
rb:
ab:
wb+:
rb+:


"""

# write: it will write a single line
# writelines: we can write multiple lines
# read: it will read all the data in single string
# readline: it will read only one line at once
# readlines: it will read all the lines and it will return a list of lines


"""
# obj = open("demo.txt", "w")

obj.write("hello I am learning file handling concept from begining.\n")
obj.write("hello I am learning file handling concept.\n")
obj.writelines(["third line\n", "fourth line\n", "fifth line\n"])
# write lines is used to write more lines in one list
# obj.close()

"""

def write_file_with_data(filename, mode):
    try:
        obj = open(filename, mode)
        obj.write("Learning file handlings along with exception handling mechanism")
    except PermissionError as e:
        print("got the exception", e)
    except FileNotFoundError as e:
        print("got the exception", e)
    finally:
        obj.close()

write_file_with_data("learn.txt", "w")


def file_operations(filepath, mode):
    try:
        if mode == "w":
            obj = open(filepath, mode)
            obj.write("Hello File with write mode1\n")
            obj.write("Hello File with write mode2\n")
            obj.write("Hello File with write mode3\n")
            obj.write("Hello File with write mode4\n")
            obj.write("Hello File with write mode5\n")

        elif mode == "r":
                obj = open(filepath, mode)
                print(obj.read())
    except FileNotFoundError as e:
        print("Got the exception:", e)
    finally:
        obj.close()
file_operations("demo1.txt", "w")
file_operations("demo1.txt", "r")

# how many specific word count in a file?
# Ans:

def file_operations(filepath, mode):
    try:
        if mode == "w":
            obj = open(filepath, mode)
            obj.write("Hello File with write mode1\n")
            obj.write("Hello File with write mode2\n")
            obj.write("Hello File with write mode3\n")
            obj.write("Hello File with write mode4\n")
            obj.write("Hello File with write mode5\n")

        elif mode == "r":
                obj = open(filepath, mode)
                # print(obj.read()) # it will read all the data from the buffer
                # print(data.count("Hello")) is used to count how many times are there in the list
                print(obj.readlines()) # it will return all the data
                print(obj.readline())
    except FileNotFoundError as e:
        print("Got the exception:", e)
    finally:
        obj.close()
file_operations("demo2.txt", "w")
file_operations("demo2.txt", "r")


# used with open
with open("demo.txt", "r") as rd:
    print(rd.read())
# no need to close the file externally.



# with open("python.jpg", "rb") as rd:
#     print(rd.read())

obj = open("python.jpg", "rb")
data = obj.read()
obj1 = open("python1.jpg", "wb")
obj1.write(data)

# tell(): by using tell I can get the current curser position
# seek(): by using seek we can set the curser position
"""

with open("demo3.txt", "w") as wd:
    wd.write("hello\n")
    print(wd.tell())
    wd.seek(1)
    print(wd.tell())
    wd.write("First")

"""


with open("demo.txt", "r") as rd:
    rd.seek(7)
    print(rd.read())

print(rd.closed)

obj = open("demo.txt")
print(obj.closed)




with open("demo1.txt", "r") as rd:
    data = rd.readlines()
    print(data[3])































