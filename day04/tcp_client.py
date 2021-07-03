"""
    tcp客户端程序
    重点代码
"""
from socket import *

# 创建tcp套接字
sockfd = socket()

# 发起连接
server_addr = ("127.0.0.1", 8888)
sockfd.connect(server_addr)
while True:
    # 收发消息
    try:
        data = input("请输入需要发送内容：\n")
        sockfd.send(data.encode())
        if not data:
            break
        data = sockfd.recv(1024)
        print("From server:", data)
    except KeyboardInterrupt:
        # 关闭
        sockfd.close()
sockfd.close()
