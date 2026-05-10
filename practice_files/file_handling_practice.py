"""
file handling:
"""


obj = open("content.txt", "w")
obj.write("Hello guys welcome back to our channel\n")
# obj.writelines(["like\n", "share\n", "subscribe"])
# writelines is used to store multiple data in a single list
obj.close()

"""
write a file with data using exception handlings
"""
def write_file_with_data(filename, mode):
    try:
        obj = open(filename, mode)
        obj.write("learning python")
    except PermissionError as e:
        print("got exception", e)
    except FileNotFoundError as e:
        print("got exception", e)
    finally:
        obj.close()
write_file_with_data("context1.txt", "w")


"""
write a program using readline, readlines
"""
def file_operation(filepath, mode):
    try:
        if mode == "w":
            obj = open(filepath, mode)
            obj.write("Hi I am Nageswari\n")
            obj.write("Hi I am Nageswari devi\n")
            obj.write("Hi I am Villa Nageswari devi\n")
            obj.write("Hi I am Nandha naidu villa")
        elif mode =="r":
            obj = open(filepath, mode)
            # print(obj.read())
            print(obj.readline())
            print(obj.readlines())
    except FileNotFoundError as e:
        print("Got the Exception", e)
    finally:
        obj.close()
file_operation("content2.txt", "w")
file_operation("content2.txt", "r")


# used with open
with open("content2.txt", "r") as rd:
    print(rd.read())
# no need to close the file externally

obj = open("python.jpg", "rb")
data = obj.read()
obj1 = open("python1.jpg", "wb")
obj1.write(data)

# tell(): by using tell we can get current curser position
# seek(): by using seek we can set the curser position

"""
with open("content.txt", "w") as wd:
    wd.write("hello\n")
    print(wd.tell())
    wd.seek(1)
    print(wd.tell())
    wd.write("First")

"""

with open("content2.txt","r") as rd:
    rd.seek(2)
    print(rd.read())

print(rd.close())

obj = open("content2.txt")







