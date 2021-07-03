"""
    multiprocess实例
"""
import multiprocessing as mp
from time import sleep


def fun():
    print("子程序开始执行")
    sleep(3)
    print("子进程执行完毕")


# 创建进程对象
p = mp.Process(target=fun)

# 启动进程
p.start()
sleep(2)
print("主进程干点事")
# 回收进程
p.join()
