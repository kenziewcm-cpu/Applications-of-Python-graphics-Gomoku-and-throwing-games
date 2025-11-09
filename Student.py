#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import*
from graphics import*



    
class Student2:
    def __init__(self,win,width1,height1):
        c0=randrange(25,60)
        c1=randrange(115,125)
        self.student=Image(Point(c0,c1),"shame2.gif")
        
        self.student.draw(win)
        
class Student3:
    def __init__(self,win,width1,height1):
        c2=randrange(82,200)
        c3=randrange(50,55)
        self.student=Image(Point(c2,c3),"shame3.gif")
        
        self.student.draw(win)       
        
        
class Student4:
    def __init__(self,win,width1,height1):
        c2=randrange(20,100)
        c3=randrange(25,35)
        self.student=Image(Point(c2,c3),"stu1.gif")
        
        self.student.draw(win)    
        
        
class Student5:
    def __init__(self,win,width1,height1):
        c2=randrange(20,70)
        c3=randrange(65,75)
        self.student=Image(Point(c2,c3),"stu2.gif")
        
        self.student.draw(win)    
class Student6:
    def __init__(self,win,width1,height1):
        c2=randrange(90,120)
        c3=randrange(85,95)
        self.student=Image(Point(c2,c3),"stu3.gif")
        
        self.student.draw(win)      
class Student7:
    def __init__(self,win,width1,height1):
        c2=randrange(170,200)
        c3=randrange(85,95)
        self.student=Image(Point(c2,c3),"stu4.gif")
        
        self.student.draw(win)           
        
class Student:
    def __init__(self,win,width1,height1):
        self.c4=randrange(25,200)
        self.c5=randrange(25,125)
        self.student=Image(Point(self.c4,self.c5),"shame.gif")
        
        self.student.draw(win)
        

    def getRandx(self):
        return self.c4

    def getRandy(self):
        return self.c5
        