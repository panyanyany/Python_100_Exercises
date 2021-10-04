import os
import sys
import time
import threading


def stop():
    # sys.exit()  # 退出线程
    # exit() # 退出线程
    # raise SystemExit # 退出线程
    # quit()  # 退出线程

    os._exit(0)  # 退出进程


while True:
    print('hello')
    threading.Thread(target=stop).start()
    # stop()
    time.sleep(.5)
