from threading import Thread, RLock
import time

num = 0  # 共享资源
lock = RLock()


class MyThread(Thread):
    def fun(self):
        global num
        with lock:
            num -= 1

    def fun2(self):
        global num
        if lock.acquire():
            num += 1
            if num > 5:
                self.fun()
            print("Num = ", num)
            lock.release()

    def run(self):
        while True:
            time.sleep(2)
            self.fun2()


t = MyThread()
t.start()
t.join()
