"""
    信号方法处理僵尸
"""
import os
import signal

# 处理子进程退出
signal.signal(signal.SIGCHLD, signal.SIG_IGN)  # 子进程发出推出信号后，父进程进行忽略

pid = os.fork()
if pid < 0:
    pass
elif pid == 0:
    print("Child PID:", os.getpid())
else:
    while True:
        pass
