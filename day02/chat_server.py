"""
    服务端
Chat room
env:python 3.6.1
socket fork 练习
"""
from socket import *
import os, sys

# def set_udp():
#     # 　创建数据报套接字
#     sockfd = socket(AF_INET, SOCK_DGRAM)
#
#     # 　绑定地址
#     server_addr = ('127.0.0.1', 8880)
#     sockfd.bind(server_addr)
#     return sockfd
server_addr = ('0.0.0.0', 8889)
dir_user = {}


def do_chat(sockfd, name, text):
    msg = '%s : %s' % (name, text)
    for i in dir_user:
        if i != name:
            sockfd.sendto(msg.encode(), dir_user[i])


def do_request(sockfd):
    while True:
        data, addr = sockfd.recvfrom(1024)
        msg = data.decode().split(" ")
        if msg[0] == "L":
            do_login(sockfd, msg[1], addr)
        elif msg[0] == "C":
            text = " ".join(msg[2:])
            do_chat(sockfd, msg[1], text)
        elif msg[0] == "Q":
            if msg[1] not in dir_user:
                sockfd.sendto(b'EXIT',addr)
                continue
            do_quit(sockfd, msg[1])
        # print(data.decode())


def do_quit(scokdf, name):
    msg = "%s\n退出了聊天室" % name
    for i in dir_user:
        if i != name:
            scokdf.sendto(msg.encode(), dir_user[i])
        else:
            scokdf.sendto(b"EXIT", dir_user[i])
        del dir_user[name]


def do_login(sockfd, name, addr):
    if name in dir_user:
        sockfd.sendto("\n该用户已存在".encode(), addr)
        return
    sockfd.sendto(b'ok', addr)
    # 通知其他人
    msg = "\n欢迎%s进入聊天室" % name
    for i in dir_user:
        sockfd.sendto(msg.encode(), dir_user[i])
    dir_user[name] = addr


def send_message(sockfd):
    pass


def main():
    # 套接子
    sockfd = socket(AF_INET, SOCK_DGRAM)
    # 　绑定地址
    sockfd.bind(server_addr)
    pid = os.fork()
    if pid < 0:
        return
    elif pid == 0:
        while True:
            msg = input("\n管理员消息：")
            msg = "C 管理员消息 " + msg
            sockfd.sendto(msg.encode(), server_addr)
    else:
        # 请求处理
        do_request(sockfd)

    # pid = os.fork()
    # if pid < 0:
    #     print("Error")
    # elif pid == 0:
    #     do_request(sockfd)
    # else:
    #     send_message(sockfd)


if __name__ == "__main__":
    main()
