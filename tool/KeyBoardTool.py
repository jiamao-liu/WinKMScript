import time
import pyautogui
class KBTool:
    def __init__(self):
        self.delay=0.02
    def pressKey(self,key,haveDelay:bool=True):
        for n in key:
            pyautogui.press(n)
            if haveDelay:
                time.sleep(self.delay)

    def downKey(self,key,haveDelay:bool=True):
        for n in key:
            pyautogui.keyDown(n)
            if haveDelay:
                time.sleep(self.delay)
    def upKey(self,key,haveDelay:bool=True):
        for n in key:
            pyautogui.keyUp(n)
            if haveDelay:
                time.sleep(self.delay)