from graphics import*
import random
from Button import*
screen=[[[0 for a in range(16)] for b in range(16)] for c in range(16)]
class OptionInterface:#用户选择模式页面
    
    def __init__(self):
        buttons=[]
        self.win1=GraphWin("模式选择",400,300)
        self.win1.setCoords(0,0,100,100)
        background = Image( Point(50,50),"choice.gif")
        background.draw(self.win1)
        self.AI=Button(self.win1,Point(30,55),40,14,"Man-Man play")#设置按钮和标题
        buttons.append(self.AI)
        self.AI.activate()
        self.human=Button(self.win1,Point(30,30),40,14,"AI-Man play")
        buttons.append(self.human)
        self.human.deactivate()
    def interact(self):
        while True:
            pt1=self.win1.getMouse()
            if self.AI.clicked(pt1):
                self.win1.close()
                return "Man-Man play"#当鼠标点击Man-Man play时，关闭页面并跳转至棋盘页面
            if self.human.clicked(pt1):
                self.win1.close()
                return "AI-Man play"
