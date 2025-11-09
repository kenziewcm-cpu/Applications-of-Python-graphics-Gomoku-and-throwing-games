from Button import*
from graphics import*
from Interface import*
from judgewin import JudgeWin
from OptionInterface import*
from piece import Piece

import random

def main():
    option=OptionInterface()
    if option.interact()== "Man-Man play":#在OptionInterface中点击按钮，跳转到该界面
        interface=Interface()#绘制棋盘交互界面
        piece=Piece()#实现在鼠标点击处，绘制棋子
        pt=interface.win.getMouse()#记录鼠标点击处点的坐标
        x,y=pt.getX(),pt.getY()
        judgewin=JudgeWin()
        black=[[0 for a in range(6)] for b in range(6)]#创建一个初始值为零的6*6的列表，存储黑棋所下的位置
        white=[[0 for a in range(6)] for b in range(6)]#创建一个初始值为零的6*6的列表，存储白棋所下的位置
            
        while True:
            while judgewin.winornot(black,white)!=1 or judgewin.winornot(black,white)!=2:
                if (len(black)+len(white))%2==0:#默认黑棋先下，通过if elif语句对于两个列表的元素个数是奇数还是偶数进行判断，进行黑白棋交替下的功能
                        pt1=interface.win.getMouse()
                        x1,y1=pt1.getX(),pt1.getY()
                        piece.put1(interface.win,pt1)
                        black[int(x1)//90-1][6-int(y1)//90]=1#将黑棋所下的位置记录为1
                        black.append(black[int(x1)//90-1][6-int(y1)//90])#在黑棋列表中加入新下的棋
                elif (len(black)+len(white))%2==1:
                        pt2=interface.win.getMouse()
                        x2,y2=pt2.getX(),pt2.getY()
                        piece.put2(interface.win,pt2)
                        white[int(x2)//90-1][6-int(y2)//90]=1#将白棋所下的位置记录为1
                        white.append(white[int(x2)//90-1][6-int(y2)//90])#在白棋列表中加入新下的棋
                            
                    
                            
                    
                
                if judgewin.winornot(black,white)==1:#返回是1，则黑棋赢了，弹出黑棋赢的提示
                    judgewin.endgameBlack()
                    break
                elif judgewin.winornot(black,white)==2:#返回是2.白棋赢了。弹出白棋赢的提示
                    judgewin.endgameWhite()
                    break
                elif len(black)+len(white)>=48:#黑白两列表元素个数判断棋盘是否被下满，弹出平局提示
                    judgewin.endgame()
                    break
            break
        interface.win.getMouse()#关闭Interface界面需要点击屏幕任意一处
        interface.close()



