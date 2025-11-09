from graphics import*
import random


class Piece:
    
    def put1(self,win,pt):
       for i in range(6):
            for j in range(6):#for循环遍历之后，对于在棋盘上点击的点的坐标，判断是在棋盘上的格子位置，在此位置上绘制出一个黑圆
                if 90*(i+1)<pt.getX()<90*(i+2) and 90*(j+1)<pt.getY()<90*(j+2):
                    
                    ci0=Circle(Point(90*i+135,90*j+135),40)
                    ci0.draw(win)
                    ci0.setFill('black')
                    
    def put2(self,win,pt):
        
        for i in range(6):
            for j in range(6):#for循环遍历之后，对于在棋盘上点击的点的坐标，判断是在棋盘上的格子位置，在此位置上绘制出一个白圆
                if 90*(i+1)<pt.getX()<90*(i+2) and 90*(j+1)<pt.getY()<90*(j+2):
                    
                    c2=Circle(Point(90*i+135,90*j+135),40)
                    c2.draw(win)
                    c2.setFill('white')
                        
