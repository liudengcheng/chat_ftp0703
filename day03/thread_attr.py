from threading import Thread
from time import sleep


def fun():
    sleep(2)
    print("test")


# 线程名称
t = Thread(target=fun, name="hehe")
t.setName("haha")
print("Thread name:", t.getName())

# 线程生命周期
print("is alive:", t.is_alive())
t.start()
print("is alive:", t.is_alive())
t.join()
print("is alive:", t.is_alive())
