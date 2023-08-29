import numpy as np
import cv2
from src.constant.KMConstant import *
import pyautogui
import time
import sys

class ImgTool:
    def __init__(self,baseDir:str="../resource/targetImg/"):
        self.baseDir=baseDir
        self.width,self.height=pyautogui.size()

    def screenshot(self,start:Point,end:Point):
        return np.array(pyautogui.screenshot(region=[start.x, start.y, end.x, end.y]))

    def read(self,path:str):
        return cv2.imread(self.baseDir+path)

    def show(self,img,title:str=' '):
        cv2.imshow(title,img)
        cv2.waitKey(0)
    def saveImg(self,filename,img):
        cv2.imwrite(filename,img)

    def findImg(self,source,target)->Point:
        sourceGray = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
        targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
        dst = cv2.matchTemplate(sourceGray, targetGray,cv2.TM_SQDIFF_NORMED)
        diff,_,(x,y),_=cv2.minMaxLoc(dst)
        print(cv2.minMaxLoc(dst))
        if diff<IMG_THRESHOLD:
            return Point(x,y)
        else:
            return Point(-1,-1)

    def operate(self,*args):
        pass

    def action(self,source1,target1,code1,delay1,source2,target2):
        for n in range(10):
            pos=self.findImg(source1,target1)
            if n==9 and pos.x==-1:
                errImg=self.screenshot(Point(0,0),Point(self.width,self.height))
                self.saveImg(code1,errImg)
                print("错误代码:"+code1+"请联系客服人员！")
                sys.exit()


        time.sleep(delay1)
        self.operate()
        self.findImg(source2,target2)
