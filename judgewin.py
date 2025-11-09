from graphics import*


class JudgeWin:
    
        
    
    def winornot(self,black,white):#判断黑白子的胜利方
        #方法返回1，则黑子胜利；方法返回2，则白子胜利
        #判断行
        for i in range(6):
            for j in range(3):
                if black[i][5-j]==1 and black[i][4-j]==1 and black[i][3-j]==1 and black[i][2-j]==1 :
                   return 1
                   break
                if white[i][5-j]==1 and white[i][4-j]==1 and white[i][3-j]==1 and white[i][2-j]==1:
                   return 2
                   break
        #判断列
        for i in range(3):
            for j in range(6):
                if black[i][5-j]==1 and black[i+1][5-j]==1 and black[i+2][5-j]==1 and black[i+3][5-j]==1:
                   return 1
                   break
                if white[i][5-j]==1 and white[i+1][5-j]==1 and white[i+2][5-j]and white[i+3][5-j]:
                   return 2
                   break
        #判断斜边
        for i in range(3):
            for j in range(3):
                if black[i][5-j]==1 and black[i+1][4-j]==1 and black[i+2][3-j]==1 and black[i+3][2-j]==1:
                   return 1
                   break
                if white[i][5-j]==1 and white[i+1][4-j]==1 and white[i+2][3-j]==1 and white[i+3][2-j]==1:
                   return 2
                   break
        for i in range(3):
            for j in range(3,6):#为使判断时，不超出列表的索引范围，使用3-5三个数即可
                if black[i][5-j]==1 and black[i+1][6-j]==1 and black[i+2][7-j]==1 and black[i+3][8-j]==1:
                   return 1
                   break
                if white[i][5-j]==1 and white[i+1][6-j]==1 and white[i+2][7-j]==1 and white[i+3][8-j]==1:
                   return 2
                   break
          
                    
                    
        
        
 
    
    def endgameBlack(self):#弹窗提示游戏结束（判断黑子赢）
        
        ww=GraphWin('提示',300,300)
        background = Image( Point(150,150),"blackwin.gif")
        background.draw(ww)
        Text(Point(150,40),'Black        Wins!').draw(ww)
        Rectangle(Point(100,260),Point(200,290)).draw(ww)
        Text(Point(150,275),"close").draw(ww)
        ww.getMouse()
        ww.close()
    def endgameWhite(self):#弹窗提示游戏结束（判断白子赢）
        
        ww=GraphWin('提示',300,300)
        background = Image( Point(150,150),"whitewin.png")
        background.draw(ww)
        Text(Point(150,40),'White        Wins!').draw(ww)
        Rectangle(Point(100,260),Point(200,290)).draw(ww)
        Text(Point(150,275),"close").draw(ww)
        ww.getMouse()
        ww.close()
    def endgame(self):#弹窗提示游戏结束（判断平局，下满平局）
        
        ww=GraphWin('提示',300,300)
        background = Image( Point(150,150),"pingju.gif")
        background.draw(ww)
        Text(Point(150,40),'Chess       Draw!').draw(ww)
        Rectangle(Point(100,260),Point(200,290)).draw(ww)
        Text(Point(150,275),"close").draw(ww)
        ww.getMouse()
        ww.close()
    
            
