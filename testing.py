import gameControll as gC
import squareControll as sC

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

def fillBoard():
    for x in range(3):
        for y in range(3):
            sC.mainBoard.x[x][y] = "X"
    
    sC.mainBoard.x[0][0] = "O"
    sC.mainBoard.x[1][2] = "O"
    sC.mainBoard.x[2][1] = "O"
    sC.mainBoard.x[1][1] = "O"