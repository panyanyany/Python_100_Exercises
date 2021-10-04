import os
import sys
import time


def stop():
    sys.exit()
    # quit()
    # exit()
    # raise SystemExit

    # os._exit(0)


while True:
    print('hello')
    stop()
    time.sleep(.5)
