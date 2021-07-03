import os
from time import sleep
print("+++++++++++++++++++++")
a=1
pid =os.fork()
if pid<0:
    print("Error")
elif pid == 0:
    print("Child process")
    print("a=%d"%a)
    a=1000
else:
    sleep(1)
    print("Parent process")
    print("a in parent process is %d"%a)
print("all a=%d"%a)