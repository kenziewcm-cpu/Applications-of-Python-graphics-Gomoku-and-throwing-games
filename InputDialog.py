from graphics import*
from Button import*
from Choke import*
from Projectile import *
class InputDialog:

    def __init__(self,angle,vel,height):
        self.win=win=GraphWin("Initial Values",300,300)
        win.setCoords(0,100,100,5)
        
        background = Image( Point(50,50),"wakeup.gif")
        background.draw(win)

        Text(Point(25,40),"Angle").draw(win)
        self.angle=Entry(Point(75,40),5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(25,50),"Velocity").draw(win)
        self.vel=Entry(Point(75,50),5).draw(win)
        self.vel.setText(str(vel))

        Text(Point(25, 60), "Height").draw(win)
        self.height = Entry(Point(75, 60), 5).draw(win)
        self.height.setText(str(height))
        
        self.fire=Button(win,Point(25,80),15,5,"Throw!")
        self.fire.activate()

        self.quit = Button(win,Point(75,80),15,5,"Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt=self.win.getMouse()
            if self.quit.clicked(pt):
                return"Quit"
            if self.fire.clicked(pt):
                return"Throw!"

    def getValues(self):
        a=float(self.angle.getText())
        v=float(self.vel.getText())
        h=float(self.height.getText())
        return a,v,h

    def close(self):
        self.win.close()