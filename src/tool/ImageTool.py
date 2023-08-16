import numpy as np
import cv2
from src.constant.KMConstant import *
import pyautogui

def screenshot(start:Point,end:Point):
    return np.array(pyautogui.screenshot(region=[start.x, start.y, end.x, end.y]))

def read(path:str):
    return cv2.imread(BASE_DIR+path)

def show(img,title:str=' '):
    cv2.imshow(title,img)
    cv2.waitKey(0)

def findImg(source,target)->Point:

    sourceGray = cv2.cvtColor(source, cv2.COLOR_RGB2GRAY)
    targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
    dst = cv2.matchTemplate(sourceGray, targetGray,cv2.TM_SQDIFF_NORMED)
    diff,_,(x,y),_=cv2.minMaxLoc(dst)
    print(cv2.minMaxLoc(dst))
    if diff<IMG_THRESHOLD:
        return Point(x,y)
    else:
        return Point(-1,-1)


