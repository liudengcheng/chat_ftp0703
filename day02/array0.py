from multiprocessing import Process, Array
from time import sleep

# c创建共享内存
# 共享内存开辟5个整
shm = Array("i", [1, 2, 3])


def fun():
    for i in shm:
        print(i)
    shm[1] = 1000


p = Process(target=fun)
p.start()
p.join()

for i in shm:
    print(i, end=" ")
