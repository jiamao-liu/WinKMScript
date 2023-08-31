import numpy as np
import cv2
import datetime
import pyautogui


from src.entity.Point import Point
from src.tool.EmailTool import SMTP
from src.tool.log import *


class ImgTool:
    def __init__(self):
        self.baseDir="C:/_check/img/"
        self.saveDir="C:/_check/log/"
        self.imgThreshold=0.3
        self.width,self.height=pyautogui.size()
        self.maxPos=Point(self.width,self.height)
        self.minPos=Point(0,0)
        self.email=SMTP()
        self.log_file = 'sys_%s.log' % datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d')
        setLog(self.saveDir+self.log_file)

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
        self.saveImg(self.saveDir+"ERRORCODE-"+str(code)+".png", errImg)
        fileList=[]
        fileList.append(self.saveDir+self.log_file)
        fileList.append(self.saveDir+"ERRORCODE-"+str(code)+".png")
        self.email.sendEmail(fileList,code)


    def findImg(self,source,target)->Point:
        sourceGray = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
        targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        dst = cv2.matchTemplate(sourceGray, targetGray,cv2.TM_SQDIFF_NORMED)
        diff,_,(x,y),_=cv2.minMaxLoc(dst)
        log(cv2.minMaxLoc(dst))
        if diff<self.imgThreshold:
            return Point(x,y)
        else:
            return Point(-1,-1)
