from graphics import*
from Button import*
from Choke import*
from Projectile import *
class InputDialog1:

    def __init__(self):
        
        self.win=win=GraphWin("You woke up the boy~~")
        win.setCoords(0,0,200,200)
        background2 = Image( Point(100,100),"hewokeup.gif")
        background2.draw(win)

        self.continue1=Button(win,Point(50,40),90,25,"Cheer up, boy")
        self.continue1.activate()

        self.quit1 = Button(win,Point(150,40),60,25,"play again")
        self.quit1.activate()

    def interact(self):
        while True:
            pt=self.win.getMouse()
            if self.quit1.clicked(pt):
                return"quit"
            if self.continue1.clicked(pt):
                return"continue1"


    def close(self):
        self.win.close()