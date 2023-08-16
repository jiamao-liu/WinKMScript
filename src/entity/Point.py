class Point:
    def __init__(self,x:int,y:int):
        self.x=x
        self.y=y
    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)
    def __str__(self):
        return "x:"+str(self.x)+"   y:"+str(self.y)

    def calculateCentor(self,other):
        o=Point(other.shape[1], other.shape[0])
        return Point(int(self.x+(o.x)/2),int(self.y+(o.y)/2))