import time
import pyautogui

def pressKey(key):
    for n in key:
        pyautogui.press(n)
        time.sleep(0.2)