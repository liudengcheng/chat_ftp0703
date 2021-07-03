import os
import time
fork_value = os.fork()
if fork_value < 0:
    print("Error")
elif fork_value == 0:
    # time.sleep(2)
    print("Child PID:", os.getpid())
    print("Get parent PID:", os.getppid())
else:
    # time.sleep(1)
    print("Parent PID:", os.getpid())
    print("Get child PID:", fork_value)
