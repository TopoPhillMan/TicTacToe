from timeit import repeat
import gameControll as gC
import squareControll as sC

def checkWin(testCondition,player): 
    for x in range(3):
        sC.mainBoard.x[testCondition][x] = player
