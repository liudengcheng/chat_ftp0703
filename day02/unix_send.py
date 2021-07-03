from socket import *

# 确保两边使用相同的套接字
sock_file = "./sock"
sockfd = socket(AF_UNIX, SOCK_STREAM)
sockfd.connect(sock_file)
while True:
    msg = input(">>")
    if not msg:
        break
    sockfd.send(msg.encode())
sockfd.close()
