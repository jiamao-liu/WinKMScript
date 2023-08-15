import time
import win32con
import win32api
from ctypes import windll

def pressKey():
    win32api.keybd_event()