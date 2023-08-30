import win32gui
import win32api
import win32con
import pyautogui

class HandleTool:
    def __init__(self):
        self.width,self.height=pyautogui.size()
    def getHandle(self,):
        return win32gui.WindowFromPoint(win32api.GetCursorPos())

    def moveHandleToRightTop(self,handle):
        win32gui.SetWindowPos(handle,win32con.HWND_TOP,int(self.width/2),0,int(self.width/2),int(self.height/2),win32con.SWP_SHOWWINDOW)

    def moveHandleToLeftTop(self,handle):
        win32gui.SetWindowPos(handle,win32con.HWND_TOP,0,0,int(self.width/2),int(self.height/2),win32con.SWP_SHOWWINDOW)

    def hiddenWindow(self,handle):
        win32gui.ShowWindow(handle,win32con.SW_SHOWMINIMIZED)
    def showWindow(self,handle):
        win32gui.ShowWindow(handle,win32con.SW_SHOWNORMAL)
