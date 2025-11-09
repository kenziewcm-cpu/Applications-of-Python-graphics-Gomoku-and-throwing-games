from graphics import*
from Projectile import *
from Button import*
from InputDialog import*
class Choke:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.maker = Rectangle(Point(0, height),Point(3,height+6))
        self.maker.setFill("white")

        self.maker.draw(win)

    def update(self, dt):
        self.proj.update(dt)
        
        dx = self.proj.getX() 
        dy = self.proj.getY() 
        self.maker.move(dx, dy)



    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw(self):
        self.maker.undraw()


        return self.rookie

