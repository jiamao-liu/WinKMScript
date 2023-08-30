from src.tool.ImageTool import *
from src.tool import MouseTool as mt
class MoveAndClick(ImgTool):
    def __init__(self):
        super().__init__()
        self.findDelay=0.3
        self.imgThreshold=0.03
    def operate(self,pos):
        mt.move(pos)
        mt.clickLeft()