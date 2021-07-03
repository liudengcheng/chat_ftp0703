"""
    select 函数讲解
"""
from socket import *
from select import select

# IO作为监控
s = socket()
s.bind(("0.0.0.0", 9999))
s.listen(3)
print('开始提交监控的IO')
rs, ws, xs = select([s], [], [])

print("rs",rs)
print("ws",ws)
print("xs",xs)