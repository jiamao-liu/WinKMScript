import pyautogui
class Point:
    def __init__(self,x,y):
        width,height=pyautogui.size()
        if isinstance(x,int):
            self.x=x
            self.y=y
        elif isinstance(x,float):
            self.x=int(width*x)
            self.y=int(height*y)

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return "x:"+str(self.x)+"   y:"+str(self.y)

    def calculateCentor(self,img):
        self.x+=int(img.shape[1]/2)
        self.y+=int(img.shape[0]/2)
