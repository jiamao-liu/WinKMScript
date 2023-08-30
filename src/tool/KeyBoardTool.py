import time
import pyautogui
class KBTool:
    def __init__(self):
        self.delay=0.2
    def pressKey(self,key):
        for n in key:
            pyautogui.press(n)
            time.sleep(self.delay)

    def downKey(self,key):
        for n in key:
            pyautogui.keyDown(n)
            time.sleep(self.delay)
    def upKey(self,key):
        for n in key:
            pyautogui.keyUp(n)
            time.sleep(self.delay)