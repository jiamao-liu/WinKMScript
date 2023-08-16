import time
import win32con
import win32api
from ctypes import windll
import pyautogui

def pressKey(key):
    for n in key:
        pyautogui.press(n)
        time.sleep(0.2)