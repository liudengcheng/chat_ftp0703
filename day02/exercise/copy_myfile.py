"""
1. multiprocess创建两个进程，同时复制一个文件的上下两半部分，各自复制到一个新的文件里
"""

from multiprocessing import Process
import os

myfile_size = os.path.getsize("./myfile")


def copy_upper():
    myfile = open("myfile", "r")
    upper_file = open("upper_file", "w")
    while myfile.tell() < myfile_size / 2-1:
        upper_file.write(myfile.read(1))
    upper_file.close()
    myfile.close()


def copy_lower():
    lower_file = open("lower_file", "w")
    myfile = open("myfile", "r")
    myfile.seek(myfile_size // 2)
    while myfile.tell() != myfile_size:
        lower_file.write(myfile.read(64))
    lower_file.close()
    myfile.close()


p = Process(target=copy_upper)
p.start()
copy_lower()
p.join()
# copy_upper()