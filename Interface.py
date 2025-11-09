from graphics import*
import random
from Button import*
screen=[[[0 for a in range(16)] for b in range(16)] for c in range(16)]
class Interface:

    def __init__(self):#对界面进行设置
        self.win=GraphWin("四子棋",900,700)
        background = Image( Point(450,350),"棋盘.png")
        background.draw(self.win)   
        p=[[0 for a in range(20)] for b in range(20)]
 
        for i in range(8):
           for j in range(8):
                p[i+1][j+1]=Point(j*90+90,i*90+90)#使用迭代，来绘制横纵向间隔一定的棋盘

        for r in range(7):
            Line(p[r+1][1],p[r+1][7]).draw(self.win)#Point(0*90+90,r*90+90),Point(7*90+90,r*90+90)
        for s in range(7):
            Line(p[1][s+1],p[7][s+1]).draw(self.win)
        center=Circle(p[4][4],3)
        center.draw(self.win)
        center.setFill('black')#绘制棋盘上中心处小黑点
    def close(self):
        self.win.close()
