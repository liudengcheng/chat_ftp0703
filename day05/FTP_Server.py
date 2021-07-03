"""
    ftp 文件服务器
    并发网络功能
"""
import os
from time import sleep
from socket import *
from threading import Thread
import signal

# 创建监听套接字
# 全局变量
HOST = "0.0.0.0"
PORT = 8888
ADDR = (HOST, PORT)
FTP = "/home/liu1/ftp/"  # 文件库路径


class FtpServer:
    def __init__(self, connfd, FTP_PATH):
        self.connfd = connfd
        self.path = FTP_PATH

    def do_list(self):
        # files = os.listdir(self.path)
        # if not files:
        #     self.connfd.send("该文件类别为空".encode())
        #     return
        # else:
        #     self.connfd.send(b'OK')
        #     time.sleep(0.1)
        # file_list = ''
        # for file in files:
        #     if file[0] != '.' and os.path.isfile(self.path + file):
        #         # self.connfd.send(file.encode())
        #         file_list += file + '\n'
        #
        # self.connfd.send(file_list.encode())
        # # time.sleep(0.1)
        # # self.connfd.send(b"##")
        # 　获取文件列表
        files = os.listdir(self.path)
        # print(files)
        if not files:
            self.connfd.send("该文件类别为空".encode())
            return
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        fs = ''
        for file in files:
            if file[0] != '.' and \
                    os.path.isfile(self.path + file):
                fs += file + '\n'
        self.connfd.send(fs.encode())

    def do_get(self, filename):
        try:
            fd = open(self.path + filename, 'rb')
        except IOError:
            self.connfd.send('文件不存在'.encode())
        else:
            self.connfd.send(b'OK')
            sleep(0.1)
        while True:
            data = fd.read(1024)
            if not data:
                sleep(0.1)
                self.connfd.send(b'##')
                break
            self.connfd.send(data)

    def do_put(self, filename):
        if filename in os.listdir(self.path):
            self.connfd.send('文件已存在'.encode())
            return
        self.connfd.send(b"OK")

        fd = open(self.path + filename, "wb")
        while True:
            data = self.connfd.recv(1024)
            if data == b'##':
                break
            fd.write(data)
        fd.close()


def handle(connfd):
    # print(connfd.recv(1024))
    cls = connfd.recv(1024).decode()
    FTP_PATH = FTP + cls + "/"
    ftp = FtpServer(connfd, FTP_PATH)
    while True:
        data = connfd.recv(1024).decode()
        # print(FTP_PATH, data)
        if not data or data[0] == 'Q':
            return
        elif data[0] == 'L':
            ftp.do_list()
        elif data[0] == "G":
            filename = data.split(" ")[-1]
            ftp.do_get(filename)
        elif data[0] == "P":
            filename = data.split(" ")[-1]
            ftp.do_put(filename)


def main():
    sockfd = socket()  # tcp套接字
    sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    sockfd.bind(ADDR)
    sockfd.listen(3)
    # 僵尸进程处理
    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    print("Listen the port 8888...")
    # 循环等待客户端链接
    while True:
        try:
            connfd, addr = sockfd.accept()
        except KeyboardInterrupt:
            sys.exit("服务器退出")
        except Exception as e:
            print(e)
            continue
        # 创建子进程处理客户端请求
        print("连接的客户端为：", addr)
        client = Thread(target=handle, args=(connfd,))
        client.setDaemon(True)  # 分支进程随主进程退出
        client.start()


if __name__ == "__main__":
    main()
