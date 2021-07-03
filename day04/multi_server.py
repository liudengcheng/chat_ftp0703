"""
    多线程
"""
from socket import *
from multiprocessing import Process
import signal

# 创建监听套接字
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)


# 客户端处理函数
def handle(c):
    print("客户端：", c.getpeername())
    while True:
        data = c.recv(1024)
        if not data:
            break
        print(data.decode())
        c.send(b"OK")
    c.close()


s = socket()  # tcp套接字
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(3)

# 僵尸进程处理
signal.signal(signal.SIGCHLD, signal.SIG_IGN)

print("Listen the port 8888...")
# 循环等待客户端链接
while True:
    try:
        c, addr = s.accept()
    except KeyboardInterrupt:
        sys.exit("服务器退出")
    except Exception as e:
        print(e)
        continue
    # 创建紫禁城处理客户端请求
    p = Process(target=handle, args=(c,))
    # p.setDaemon(True)  # 分支进程随主进程退出
    p.start()

