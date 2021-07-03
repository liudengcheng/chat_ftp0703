"""
    创建耳机子进程防止僵尸进程
"""

import os
import sys
from time import *


def child_fun():
    for i in range(4):
        sleep(1)
        print("writing code...")


def parent_fun():
    for i in range(5):
        sleep(2)
        print("testing code...")


pid = os.fork()

if pid < 0:
    print("failed")
elif pid == 0:
    p = os.fork()
    if p == 0:
        child_fun()
    else:
        sys.exit(0)
else:
    os.wait()
    parent_fun()
