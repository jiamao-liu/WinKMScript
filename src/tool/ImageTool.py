from src.entity import Point
from PIL import ImageGrab,Image

def screenshot(start:Point,end:Point)->Image:
    return ImageGrab.grab(start.x,start.y,end.x,end.y)
