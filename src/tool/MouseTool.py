import time
import win32con
import win32api
from ctypes import windll

from src.constant.KMConstant import *
from src.entity.Point import Point


def move(pos:Point):
    time.sleep(MOUSE_DELAY_TIME)
    windll.user32.SetCursorPos(pos.x,pos.y)
    time.sleep(MOUSE_DELAY_TIME)

def clickLeft():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)

    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)

def clickRight():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)

def downLeft():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)

def upLeft():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)

def downRight():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)

def upRight():
    time.sleep(MOUSE_DELAY_TIME)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
    time.sleep(MOUSE_DELAY_TIME)



