import sys
import time

from src.constant.KMConstant import *
from src.tool import ImageTool as it
from src.tool import MouseTool as mt
from src.tool import KeyBoardTool as kt




if __name__ == '__main__':
    print("程序开始！")
    xjimg=it.screenshot(start,end)
    xjTarget=it.read("img.png")
    xjPos=it.findImg(xjimg,xjTarget)
    if(xjPos.x==-1 or xjPos.y==-1):
        print("未找到新建按钮！")
        sys.exit()
    xjCPos=xjPos.calculateCentor(xjTarget)
    print(xjCPos)
    mt.move(xjCPos)
    mt.clickLeft()
    mt.clickLeft()
    time.sleep(1)
    kt.pressKey(['b','e','i','j','i','n','g','s','h','i','j','i','a','n',' '])
