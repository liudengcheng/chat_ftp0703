from threading import Thread
from time import sleep, ctime


class MyThread(Thread):
    pass


# *********************
def player(sec, song):
    for i in range(2):
        print("Playing %s:%s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,), kwargs={"song": "凉凉"}, name="happy")
t.start()
t.join()
