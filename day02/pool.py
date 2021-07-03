"""
    进程池原理实例
"""

from multiprocessing import Pool
from time import sleep, ctime


# 进程池事件
def work(msg):
    sleep(2)
    print(msg)


# 创建进程池
pool = Pool(6)

for i in range(20):
    msg = "Hello %d" % i
    pool.apply_async(func=work, args=(msg,))

# 关闭进程池
pool.close()

# 回收进程持
pool.join()
