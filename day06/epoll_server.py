"""
    IO多路复用，使用epoll实现
    次重点
"""

from socket import *
from select import *

# set socket to concern
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(5)

# create epoll
ep = epoll()

# create dictionary for poll({fileno:io_obj})
fdmap = {s.fileno(): s}
# set IO
ep.register(s, EPOLLIN | EPOLLERR)

# monitor IO event
while True:
    events = ep.poll()  # waiting for io
    # travers list and handle IO
    for fd, event in events:
        if fd == s.fileno():
            c, addr = fdmap[fd].accept()
            print("connect from", addr)
            ep.register(c, EPOLLIN | EPOLLHUP)
            fdmap[c.fileno()] = c
        # elif event & POLLHUP: # client disconnect
        #     print("客户端退出")
        #     p.unregister(fd) # unconcern the io
        #     fdmap[fd].close()  # close socket C
        #     del fdmap[fd]  # del c from dictionary
        #     continue
        elif event & EPOLLIN:
            data = fdmap[fd].recv(1024)
            if not data:
                print("客户端退出")
                ep.unregister(fd)  # unconcern the io
                fdmap[fd].close()  # close socket C
                del fdmap[fd]  # del c from dictionary
                continue
                # continue
            print(data.decode())
            fdmap[fd].send(b'OK')
