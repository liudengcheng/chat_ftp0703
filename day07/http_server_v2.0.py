"""
    http server v2.0
    *IO 并发处理
    *基本的request解析
    *使用类封装
"""

from socket import *
from select import select


class HTTPServer:
    def __init__(self, server_addr, static_dir):
        # 添加属性
        self.server_address = server_addr
        self.static_dir = static_dir
        self.create_socket()
        self.bind()
        self.rlist = self.wlist = self.xlist = []

    def create_socket(self):
        self.sockfd = socket()
        self.sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

    def bind(self):
        self.sockfd.bind(self.server_address)
        self.ip = self.server_address[0]
        self.prot = self.server_address[1]

    def serve_forever(self):
        self.sockfd.listen(5)
        print("Listen from port %d ..." % self.prot)
        self.rlist.append(self.sockfd)
        while True:
            rs, ws, xs = select(self.rlist, self.wlist, self.xlist)
            for r in rs:
                if r is self.sockfd:
                    c, addr = r.accept()
                    print("Connect from", addr)
                    self.rlist.append(c)
                else:
                    # 处理浏览器请求
                    self.handle(r)

    def handle(self, connfd):
        # 接受http请求
        request = connfd.recv(4096)
        print(request)
        # 防止浏览器断开
        if not request:
            self.rlist.remove(connfd)
            connfd.close()
            return
        # 将request按行分割
        request_line = request.splitlines()[0].decode()
        # 　获取请求内容
        info = request_line.split(' ')[1]
        print(connfd.getpeername(), ':', info)
        if info == '/' or info[-5:] == '.html':
            self.get_html(connfd, info)
        else:
            self.get_data(connfd, info)
        self.rlist.remove(connfd)
        connfd.close()

    def get_data(self, connfd, info):
        """
        其他情况
        :param connfd:
        :param info:
        :return:
        """
        response_Headers = "HTTP/1.1 200 OK\r\n"
        response_Headers += "Content-Type: text/html\r\n"
        response_Headers += '\r\n'
        response_Body = "<h1>%s can not be served, Waiting httpserver 3.0</h1>"%info
        response = response_Headers + response_Body
        connfd.send(response.encode())

    def get_html(self, connfd, info):
        """
        处理网页请求
        :param connfd:
        :param info:
        :return:
        """
        if info == '/':
            filename = self.static_dir + '/index.html'
        else:
            filename = self.static_dir + info
        try:
            fd = open(filename)
        except Exception:
            response_Headers = "HTTP/1.1 404 Not Found\r\n"
            response_Headers += "Content-Type: text/html\r\n"
            response_Headers += '\r\n'
            response_Body = "<h1>Sorry....</h1>"
        else:
            response_Headers = "HTTP/1.1 200 OK\r\n"
            response_Headers += "Content-Type: text/html\r\n"
            response_Headers += '\r\n'
            response_Body = fd.read()
        finally:
            response = response_Headers + response_Body
            connfd.send(response.encode())


# 如何使用HTTPServer类
if __name__ == "__main__":
    # 用户自己决定： 地址 ，内容
    server_addr = ('0.0.0.0', 8000)
    static_dir = './static'  # 网页存放地址
    httpd = HTTPServer(server_addr, static_dir)  # 生成实例对象
    httpd.serve_forever()  # 启动对象
