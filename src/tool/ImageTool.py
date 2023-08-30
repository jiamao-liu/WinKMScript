import numpy as np
import cv2

import pyautogui
import time
import sys

from src.entity.Point import Point
from src.tool.log import *

class ImgTool:
    def __init__(self):
        self.retry=5
        self.baseDir="../resource/targetImg/"
        self.width,self.height=pyautogui.size()
        self.findDelay=0.4
        self.saveDir="C:/"
        self.imgThreshold=0.3

        self.maxPos=Point(self.width,self.height)
        self.minPos=Point(0,0)
        self.pos1=Point(int(self.width*0.1),int(self.height*0.1))
        self.pos8=Point(int(self.width*0.8),int(self.height*0.8))

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
        print(filename)
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

    def operate(self,pos):
        pass

    def action(self,source1,target1,code1,reOperate=0,check=False,checkStart:Point=None,checkEnd:Point=None,target2=None,code2=-1):
        if checkStart==None:
            checkStart=self.minPos
        if checkEnd==None:
            checkEnd=self.maxPos

        for n in range(self.retry):
            pos=self.findImg(source1,target1)
            if n==self.retry-1 and pos.x==-1:
                self.errorProcess(code1)
                log("寻找图像出现错误，错误代码："+str(code1))
                sys.exit()
            elif pos.x==-1:
                time.sleep(self.findDelay*3)
            else:
                break

        self.operate(pos)
        if check==False:
            return
        for n in range(self.retry):
            source2=self.screenshot(checkStart,checkEnd)
            over=self.findImg(source2,target2)
            log(over)
            if n==self.retry-1 and over.x==-1:
                self.errorProcess(code2)
                log("寻找图像出现错误，错误代码："+str(code2))
                sys.exit()
            elif over.x==-1:
                time.sleep(self.findDelay)
                if reOperate!=0 and (n+1)%reOperate==0:
                    self.operate(pos)
            else:
                break
