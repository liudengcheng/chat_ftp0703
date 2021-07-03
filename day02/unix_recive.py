"""
    本地套接字
"""
import os
from socket import *

# 确定本地套接字文件
sock_file = "./sock"

# 判断文件是否存在，存在就删除
if os.path.exists(sock_file):
    os.remove(sock_file)
# 创建本地套接字
sockfd = socket(AF_UNIX, SOCK_STREAM)

# 绑定本地套接字
sockfd.bind(sock_file)

# 监听，链接
sockfd.listen(3)

while True:
    try:
        c, addr = sockfd.accept()
        while True:
            data = c.recv(1024)
            if not data:
                break
            print(data.decode())
        c.close()
    except KeyboardInterrupt:
        break
sockfd.close()
