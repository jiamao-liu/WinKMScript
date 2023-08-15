import time
import win32con
import win32api
from ctypes import windll

from src.constant import Constant
from src.entity.Point import Point


def move(pos:Point):
    time.sleep(Constant.OPERATE_DELAY_TIME)
    windll.user32.SetCursorPos(pos.x,pos.y)
    time.sleep(Constant.OPERATE_DELAY_TIME)

def clickLeft():
    time.sleep(Constant.OPERATE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(Constant.OPERATE_DELAY_TIME)

def clickRight():
    time.sleep(Constant.OPERATE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    time.sleep(Constant.OPERATE_DELAY_TIME)




