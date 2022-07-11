import gameControl as gC
import squareControl as sC

def checkWin(testCondition,deffiner,player): 
    if testCondition == 0:
        for x in range(3):
            sC.mainBoard.x[deffiner][x] = player
    if testCondition == 1:
        for x in range(3):
            sC.mainBoard.x[x][deffiner] = player
    if testCondition == 2:
        if deffiner == 0:
            sC.mainBoard.x[0][0] == player
            sC.mainBoard.x[1][1] == player
            sC.mainBoard.x[2][2] == player
        if deffiner == 1:
            sC.mainBoard.x[2][0] == player
            sC.mainBoard.x[1][1] == player
            sC.mainBoard.x[0][2] == player

def fillBoard(xRows, yRows):
    for y in range(yRows):
        for x in range(xRows):
            sC.mainBoard.x[y].x[x] = "X"

def checkOrientation():
    sC.mainBoard.x[1][1] = "◁"
    sC.mainBoard.x[2][1] = "◁"



