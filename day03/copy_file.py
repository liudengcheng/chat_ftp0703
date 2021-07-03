from multiprocessing import Process
import os

filename = "./index.jpeg"
# 获取图片大小
size = os.path.getsize(filename)


# copy top
def top():
    f = open(filename, 'rb')
    n = size // 2
    fw = open("top.jpeg", 'wb')
    fw.write(f.read(n))
    f.close()
    fw.close()


# copy bottle
def bot():
    f = open(filename, 'rb')
    fw = open('bot.jpeg', 'wb')
    f.seek(size // 2, 0)
    while True:
        data = f.read(1024)
        if not data:
            break
        fw.write(data)
    f.close()
    fw.close()


t = Process(target=top)
b = Process(target=bot)
t.start()
b.start()
t.join()
b.join()
