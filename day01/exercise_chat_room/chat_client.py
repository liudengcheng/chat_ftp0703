"""
   客户端
"""
from socket import *
import os, sys

# 服务器地址
ADDR = ("192.168.197.130", 8889)


# 创建网络链接
def main():
    sockfd = socket(AF_INET, SOCK_DGRAM)
    while True:
        name = input("请输入姓名：\n")
        msg = "L " + name
        sockfd.sendto(msg.encode(), ADDR)
        data, addr = sockfd.recvfrom(1024)
        if data.decode() == "ok":
            print("您已进入聊天室")
            break
        else:
            print(data.decode())
    # create a new process
    pid = os.fork()
    if pid < 0:
        sys.exit("Error!")
    elif pid == 0:
        send_msg(sockfd, name)
    else:
        recv_msg(sockfd)


# 发送消息
def send_msg(sockfd, name):
    while True:
        try:
            text = input("发言：\n")
        except KeyboardInterrupt:
            text = 'quit'
        if text == 'quit':
            msg = "Q " + name
            sockfd.sendto(msg.encode(), ADDR)
            sys.exit("退出聊天室")
        if text:
            msg = 'C %s %s' % (name, text)
            sockfd.sendto(msg.encode(), ADDR)


# 接受信息
def recv_msg(sockfd):
    while True:
        data, addr = sockfd.recvfrom(2048)
        if data.decode() == "EXIT":
            sys.exit()
        print(data.decode())


if __name__ == "__main__":
    main()
