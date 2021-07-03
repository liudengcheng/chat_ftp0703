"""
    线程示例


"""
import multiprocessing
import threading
import time, os

a = 1


# 线程函数
def music():
    global a
    for i in range(5):
        time.sleep(2)
        print("播放心如治水%d" % os.getpid())
        print("a=",a)
        a = 3
    # 创建县城对象


t = threading.Thread(target=music)
# t = multiprocessing.Process(target=music)
t.start()
# music()
# 主线程任务
for i in range(3):
    time.sleep(3)
    print("播放跳舞吧%d" % os.getpid())
t.join()  # 回收线程
print("Main thread a:", a)
