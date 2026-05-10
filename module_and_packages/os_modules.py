# Modules:

# module: It is a kind of python file, it can contain classes functions, variables, etc.
# module is a grouping the functions.
# os, datetime, re, json, functools

# import os
# print(type(os))
# print(dir(os))
# 'chdir', 'chmod', 'close', 'closerange', 'cpu_count', 'curdir', 'defpath', 'device_encoding', 'devnull',
# 'dup', 'dup2', 'environ', 'error', 'execl', 'execle', 'execlp', 'execlpe', 'execv', 'execve', 'execvp',
# 'execvpe', 'extsep', 'fchmod', 'fdopen', 'fsdecode', 'fsencode', 'fspath', 'fstat', 'fsync', 'ftruncate',
# 'get_blocking', 'get_exec_path', 'get_handle_inheritable', 'get_inheritable', 'get_terminal_size', 'getcwd',
# 'getcwdb', 'getenv', 'getlogin', 'getpid', 'getppid', 'isatty', 'kill', 'lchmod', 'linesep', 'link', 'listdir',
# 'listdrives', 'listmounts', 'listvolumes', 'lseek', 'lstat', 'makedirs', 'mkdir', 'name', 'open', 'pardir',
# 'path', 'pathsep', 'pipe', 'popen', 'process_cpu_count', 'putenv', 'read', 'readlink', 'remove', 'removedirs',
# 'rename', 'renames', 'replace', 'rmdir', 'scandir', 'sep', 'set_blocking', 'set_handle_inheritable',
# 'set_inheritable', 'spawnl', 'spawnle', 'spawnv', 'spawnve', 'st', 'startfile', 'stat', 'stat_result',
# 'statvfs_result', 'strerror', 'supports_bytes_environ', 'supports_dir_fd', 'supports_effective_ids',
# 'supports_fd', 'supports_follow_symlinks', 'symlink', 'sys', 'system', 'terminal_size', 'times', 'times_result',
# 'truncate', 'umask', 'uname_result', 'unlink', 'unsetenv', 'urandom', 'utime', 'waitpid', 'waitstatus_to_exitcode',
# 'walk', 'write']

"""
try:
    print(os.getcwd())  # get current working directory
    os.mkdir("Nandha")  # it will create a directory
except FileExistsError:
    print("Already file is there")
    os.chdir("Nandha") # change directory
    print(os.getcwd())

"""

import os
print(os.getcwd()) # get current working directory
print(os.listdir()) # is a function is used to list all files and directories in a specified path.
print(os.path.isfile("os_modules.py")) # it will returns the file is there it will print True
# is not there it will print false
# os.mkdir("Nandha_naidu_villa")  #it will create a directory
print(os.path.isdir("Nandha_naidu_villa")) # it will returns the directory is there it will print True
# otherwise it will print false
os.chdir("Nandha_naidu_villa") # is used to change the current working directory to a different folder.
print(os.getcwd())

with open("Nandha_naidu_villa_1.txt", "w") as wr:
    wr.write("I am learning python")
# os.system("cd . .")
print(os.getcwd())
# print(os.path.join()) #
print(os.getenv("path")) # it will returns path

# how to find the only text files from the folder and it's subfolder?
# for dir, subdir, file in os.walk("C:\Users\Dell\PycharmProjects\PythonProject"): #
# walk method is used to travels from all the folders and sub folders
#     print("DIR", dir)
#     print("SUB DIR", subdir)
#     for f in file:
#         if f.endswith(".txt"): #
#             print("File:", f)
            



# How we can create nested dir means multiple dic

# os.mkdir("demo4")
# if not os.path.isdir("demo1/demo2/demo3"):
#     os.makedirs("demo1/demo2/demo3")
# os.rmdir("demo4") # remove dir
# os.rmdir("demo1/demo2/demo3") # it will remove last dir
# os.remove("Nandha_naidu_villa_1.txt")
# os.rename("demo1", "demo") # it is used to change the dir name

# print(os.system("dir")) # it will returns all the details in file format
# data = os.popen("dir")
# print(data.read())

print(os.getenv("path"))
print(os.getenv("TEMP"))
print(os.environ)
# os.putenv()















































