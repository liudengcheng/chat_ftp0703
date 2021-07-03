import os
import sys

pid = os.fork()

if pid < 0:
    print("failed")
elif pid == 0:
    print("Child process", os.getpid())
    sys.exit(2)

else:
    pid, status = os.wait()
    # pid, status = os.waitpid(-1, os.WNOHANG)
    print("PID:", pid)
    print("status:", status/256)
    while True:
        pass
