import threading
from helper import *


class MyThread(threading.Thread):
    def __init__(self, hwnd, lock):
        super(MyThread, self).__init__()
        self._hwnd = hwnd
        self._lock = lock

    def run(self):
        self.__main_loop()

    def getName(self):
        return self.name

    def __main_loop(self):
        img_file = './img/OVERFLOW.bmp'
        index = 0
        while True:
            index += 1
            print("线程%s第%d次截图" % (self.getName(), index))
            with self._lock:
                img_src = screen_shot(self._hwnd)
