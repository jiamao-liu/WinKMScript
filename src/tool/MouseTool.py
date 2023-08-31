import time
import win32con
import win32api
from ctypes import windll

from src.entity.Point import Point


class MouseTool:
    def __init__(self):
        self.delay=0.2
    def move(self,pos:Point,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        windll.user32.SetCursorPos(pos.x,pos.y)
        if haveDelay:
            time.sleep(self.delay)
    def clickLeft(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)

    def clickRight(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)

    def downLeft(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)

    def upLeft(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)

    def downRight(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)

    def upRight(self,haveDelay:bool=True):
        if haveDelay:
            time.sleep(self.delay)
        win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0,0,0)
        if haveDelay:
            time.sleep(self.delay)



