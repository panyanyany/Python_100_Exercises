import os
import sys
import time


def stop():
    # sys.exit()
    # quit()
    # exit()
    # raise SystemExit

    os._exit(0)


while True:
    print('hello')
    try:
        stop()
    except SystemExit as e:
        print('接收到退出命令:', type(e))
    time.sleep(.5)
