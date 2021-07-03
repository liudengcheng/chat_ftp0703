"""
    套接字非阻塞示例
"""
from socket import *
from time import sleep, ctime

# 用文件记录报错
fd = open('log.txt', 'a')

# tcp套接字
sockfd = socket()
sockfd.bind(('127.0.0.1', 8880))
sockfd.listen(3)

# 设置套接字为非阻塞
# sockfd.setblocking(False)

# 超时检测
sockfd.settimeout(3)

while True:
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
    except Exception as e:
        sleep(2)
        fd.write("%s :%s\n" % (ctime(), e))
        fd.flush()
    else:
        data = connfd.recv(1024).decode()
        print(data)
