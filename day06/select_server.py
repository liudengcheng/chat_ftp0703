"""
    IO多路复用select实现客户端通

"""
from socket import *
from select import select

# set socket to concern
s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(("0.0.0.0", 8888))
s.listen(5)

# set concerned IO
rlist = [s]
wlist = []
xlist = []

while True:
    # monitor IO
    rs, ws, xs = select(rlist, wlist, xlist)
    # traverse return list, find which happened
    for r in rs:
        # if the socket is ready, handle it.
        if r is s:
            c, addr = r.accept()
            print("connect from", addr)
            rlist.append(c)  # add a new concerned IO
        else:
            data = r.recv(1024)
            if not data:
                rlist.remove(r)
                r.close()
                continue
            print(data)
            # r.send(b'OK')
            # we wish to handle the IO by wlist
            wlist.append(r)
    for w in ws:
        w.send(b'Ok,Thanks')
        wlist.remove(w)
    for x in xs:
        pass
