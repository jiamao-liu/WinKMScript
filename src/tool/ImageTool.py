import numpy as np
import cv2

import pyautogui
import time
import sys

from src.entity.Point import Point
from src.tool.log import *

class ImgTool:
    def __init__(self):
        self.baseDir="C:/_check/img/"
        self.saveDir="C:/_check/log/"
        self.imgThreshold=0.3
        self.width,self.height=pyautogui.size()
        self.maxPos=Point(self.width,self.height)
        self.minPos=Point(0,0)

    def screenshot(self,start:Point=None,end:Point=None):
        if start==None:
            start=self.minPos
        if end==None:
            end=self.maxPos
        return np.array(pyautogui.screenshot(region=[start.x, start.y, end.x, end.y]))

    def read(self,path:str):
        return cv2.imread(self.baseDir+path)

    def show(self,img,title:str=' '):
        cv2.imshow(title,img)
        cv2.waitKey(0)
    def saveImg(self,filename,img):
        cv2.imwrite(filename,img)

    def errorProcess(self,code=0):
        errImg = self.screenshot()
        self.saveImg(self.saveDir+"错误代码"+str(code)+".png", errImg)

    def findImg(self,source,target)->Point:
        sourceGray = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
        targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        dst = cv2.matchTemplate(sourceGray, targetGray,cv2.TM_SQDIFF_NORMED)
        diff,_,(x,y),_=cv2.minMaxLoc(dst)
        print(cv2.minMaxLoc(dst))
        if diff<self.imgThreshold:
            return Point(x,y)
        else:
            return Point(-1,-1)
