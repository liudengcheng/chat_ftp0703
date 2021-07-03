"""
    fork势力
"""
import os
import time

pid = os.fork()

if pid < 0:
    print("failed")
elif pid == 0:
    # time.sleep(1)
    time.sleep(1)
    print("New process")
else:
    time.sleep(2)
    print("old process")
print("finished")
