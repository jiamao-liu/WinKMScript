import time
import win32con
import win32api
from ctypes import windll

from src.entity.Point import Point


def move(pos:Point):
    time.sleep(0.05)
    windll.user32.SetCursorPos(pos.x,pos.y)
    time.sleep(0.05)

def clickLeft():
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(0.05)

def clickRight():
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    time.sleep(0.05)




