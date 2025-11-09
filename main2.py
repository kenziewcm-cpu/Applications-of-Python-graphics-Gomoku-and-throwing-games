#!/usr/bin/env python
# coding: utf-8

# In[1]:




import random
from math import *
from graphics import *
from Student import *
from InputDialog1 import *


# In[2]:



class ShotTracker:
    def __init__(self, win, angle, velocity, height):
        self.proj = Projectile(angle, velocity, height)
        self.marker = Rectangle(Point(20, height),Point(22,height+6))
        self.marker.setFill("white")

        self.marker.draw(win)

    def update(self, dt):
        self.proj.update(dt)

        center = self.marker.getCenter()
        dx = self.proj.getX() - center.getX()
        dy = self.proj.getY() - center.getY()
        self.marker.move(dx, dy)

    def getX(self):
        return self.proj.getX()

    def getY(self):
        return self.proj.getY()

    def undraw(self):
        self.marker.undraw()






class Target:
    def __init__(self, win, randomx,randomy):
        self.xmax, self.xmin = randomx + 50, randomx - 50
        self.ymax, self.ymin = randomy+50,randomy-50
#        p1 = Point(self.xmin, self.ymin)
#        p2 = Point(self.xmax, self.ymax)



# In[ ]:


class InputDialog:

    def __init__(self,angle,vel):
        self.win=win=GraphWin("Initial Values",300,300)
        win.setCoords(0,100,100,5)
        
        background = Image( Point(50,50),"wakeup.gif")
        background.draw(win)

        Text(Point(25,42),"Angle").draw(win)
        self.angle=Entry(Point(75,42),5).draw(win)
        self.angle.setText(str(angle))

        Text(Point(25,60),"Velocity").draw(win)
        self.vel=Entry(Point(75,60),5).draw(win)
        self.vel.setText(str(vel))

#        Text(Point(25, ), "Height").draw(win)
#        self.height = Entry(Point(75, 60), 5).draw(win)
#        self.height.setText(str(height))
        
        self.fire=Button(win,Point(25,80),15,5,"Throw!")
        self.fire.activate()

        self.quit = Button(win,Point(75,80),15,5,"Quit")
        self.quit.activate()

    def interact(self):
        while True:
            pt = self.win.getMouse()
            if self.quit.clicked(pt):
                return "Quit"
            if self.fire.clicked(pt):
                return "Fire!"
    def getValues(self):
        a = float(self.angle.getText())
        v = float(self.vel.getText())
     #   h = float(self.height.getText())
        return a, v

    def getMouse(self):
        self.win.getMouse()

    def close(self):
        self.win.close()




# In[3]:



class Button:
    def __init__(self,win,center,width,height,label):
        w,h=width/2.0,height/2.0
        x,y=center.getX(),center.getY()
        self.xmax, self.xmin = x + w, x - w
        self.ymax, self.ymin = y + h, y - h
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)
        self.rect = Rectangle(p1, p2)
        self.rect.setFill('lightgray')
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()
    def clicked(self, p):
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill('black')
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill('darkgray')
        self.rect.setWidth(1)
        self.active = False


# In[4]:


class Projectile:
    def __init__(self, angle, velocity, height):
        self.xpos = 20.0
        self.ypos = height
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity *sin(theta)

    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - 9.8 * time
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1  # 这一句在前一句后面执行是必要的，否则yvelo原值将被覆盖，无法求出平均速度，进而无法计算位移

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos


# In[8]:


def main2(self):
    win = GraphWin("Wake up the sleeping student", 640, 480, autoflush=False)
    win.setCoords(-10, -10, 210, 155)
    background = Image( Point(100,72.5),"classroom.gif")
    background.draw(win)
    text1=Text(Point(100,150),"welcome to this class").draw(win)
    text2=Text(Point(100,142),"You are professor").draw(win)
    
    angle=Entry(Point(130,142),5)
    angle.setText("Wang")

    
    angle.draw(win)
    text3=Text(Point(150,136),"(press 'escape' to confirm)").draw(win)
    
    
    
    while True:
        key=win.getKey()
        if key =="Escape":
            break
    you=angle.getText()
    
    test2=Text(Point(130,142),you).draw(win)    
    angle.undraw()
    text3.undraw()
    
    text7=Text(Point(100,20),"You are teaching a new lesson(click here)").draw(win)
    e=win.getMouse()
    text8=Text(Point(100,10),"Suddenly you notice someone snoring(click)").draw(win)
    r=win.getMouse()

    target2=Student2(win,50,25)

    target5=Student5(win,50,25)    
    target6=Student6(win,50,25)
    target7=Student7(win,50,25)
    target3=Student3(win,50,25)
    target4=Student4(win,50,25)
    target1=Student(win,50,25)
    xs=target1.getRandx()
    ys=target1.getRandy()
    


    
    text5=Text(Point(100,134),"     Find out the sleeping student!!")
    text6=Text(Point(100,128),"     (press 'escape'and click the sleeping student you've found)")
    text5.draw(win)
    text6.draw(win)    
    while True:
        key=win.getKey()
        if key =="Escape":
            break

    
    m=win.getMouse()
    mx=m.getX()
    my=m.getY()
    
    
    if mx-20<=xs<=mx+20 and my-20<=ys<=my+20 :
        test2.undraw()
        angle.undraw()
        text5.undraw()
        text6.undraw()
        text7.undraw()
        text8.undraw()
        text1.undraw()
        text2.undraw()
        angle.undraw()
        Text(Point(100,140),"You find him!!").draw(win) 
        Text(Point(100,130),"Now wake him up with your chalk,professor "+you).draw(win) 
        Text(Point(40,42),"   Here is your chalk").draw(win)
        Text(Point(40,37),"   Throw it!!!").draw(win)
        
        m4=Circle(Point(mx,my),15).draw(win)
        

        
    else:
        test2.undraw()
        angle.undraw()
        text5.undraw()
        text6.undraw()
        text7.undraw()
        text8.undraw()
        text1.undraw()
        text2.undraw()
        angle.undraw()
        Text(Point(mx,my+10),"Not this guy").draw(win)
        m5=Circle(Point(xs,ys+9),15).draw(win)
        Text(Point(xs,ys+20),"Look, here he is...").draw(win)
        Text(Point(100,142)," Now wake the sleeping boy up ").draw(win) 
        Text(Point(100,136)," using the chalk in your hand, professor "+you).draw(win) 
        Text(Point(40,42),"   Here is your chalk").draw(win)
        Text(Point(40,37),"   Throw it!!!").draw(win)

        
    for x in range(0, 210, 50):
        Text(Point(x, -5), str(x)).draw(win)
        Line(Point(x, 0), Point(x, 2)).draw(win)

    angle, vel, height = 45.0, 40, 42.0
    while True:
        inputwin = InputDialog(angle, vel)
        choice = inputwin.interact()
        inputwin.close()

        if choice == "Quit":
            break

        angle, vel = inputwin.getValues()
        
        shot = ShotTracker(win, angle, vel,height)
        while 0 <= shot.getY() and -10 < shot.getX() <= 210:


            shot.update(1 / 50)
            update(50)
            if (ys-10<=shot.getY()<=ys+10 and xs-15<=shot.getX()<=xs+15):
                shot.update(1/1)
                update(1)


                while True:
                    inputwin1 = InputDialog1()
                    choice1 = inputwin1.interact()



                    if choice1 == "quit":
                        inputwin1.close() 

                        break
                    if choice1 == "continue1":

                        win3=GraphWin("You woke up the boy~~",600,600)
                        win3.setCoords(0,0,200,200)
                        background3 = Image( Point(100,100),"hesmiles.gif")
                        background3.draw(win3)
                        
                        t1=Text(Point(30,170),"Hey boy...").draw(win3)
                        T1=win3.getMouse() 
                        t2=Text(Point(30,160),"What's going on?").draw(win3)
                        T2=win3.getMouse()                        
                        
                        s1=Text(Point(130,180),"i am SORRY,professor "+you+"...")

                        
                        s1.draw(win3)
                        S1=win3.getMouse()
                        s2=Text(Point(140,160),"i stayed up until 3:00 ").draw(win3)
                 
               
                        s3=Text(Point(140,150),"yesterday writing a paper...").draw(win3)
                        S2=win3.getMouse()
                    
                        s4=Text(Point(140,130),"I'll adjust my biological clock...").draw(win3)
                        S3=win3.getMouse()
                        
                        s5=Text(Point(150,110),"and work hard on your lesson...").draw(win3)
                        S4=win3.getMouse()
                        
                        t1.undraw()
                        t2.undraw()
                        
                        t3=Text(Point(30,170),"Good for you, kid...").draw(win3)
                        T3=win3.getMouse()      
                        t3=Text(Point(37,150),"And do not fall asleep again~~").draw(win3)
                        T4=win3.getMouse()
                        
                        
                        M=Text(Point(160,90),"   .click to exit").draw(win3)
                        M=win3.getMouse()
                        
                        win3.close()


                    inputwin1.close()  


    
        
 

#      else:
#            shot.undraw()
    win.close()


# In[9]:




