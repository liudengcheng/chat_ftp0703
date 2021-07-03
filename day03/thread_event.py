from threading import Thread, Event
from time import sleep

s = None  # 全局变量用于通讯
e = Event()  # 事件对象


def yangzirong():
    print("杨子荣前来拜山头")
    sleep(3)
    global s
    s = "天王盖地虎"
    e.set()


t = Thread(target=yangzirong)
t.start()
print("说对口令就是自己人")
e.wait()
if s == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他")

t.join()
