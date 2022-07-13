from random import random
import gameControl as gC
import squareControl as sC
import ticFunctions as tic
import connectFunctions as con
import golfFunctions as golf
import math

sC.mainBoard.xRows = 40
sC.mainBoard.yRows = 10
sC.mainBoard.x = sC.board.genBoard(sC.mainBoard.xRows, sC.mainBoard.yRows)

golf.mainBall.x = 1
golf.mainBall.y = 3
golf.mainBall.sprite = "B"
golf.mainBall.weight = 1

golf.mapBoard.xRows = sC.mainBoard.xRows
golf.mapBoard.yRows = sC.mainBoard.yRows
golf.mapBoard.x = sC.board.genBoard(golf.mapBoard.xRows, golf.mapBoard.yRows)

# golf.changeAlt(0,1,2)
# golf.addStraight(2,3,3)
# golf.changeAlt(5,3,-2)

golf.genMap()

sC.mainBoard.x = golf.mapBoard.x
sC.printBoardCombined(sC.mainBoard.yRows,sC.mainBoard.xRows)
