import gameControl as gC
import squareControl as sC
import ticFunctions as tic
import connectFunctions as con
import golfFunctions as golf
import math

sC.mainBoard.xRows = 6
sC.mainBoard.yRows = 3
sC.mainBoard.x = sC.board.genBoard(sC.mainBoard.xRows, sC.mainBoard.yRows)

golf.mainBall.x = 1
golf.mainBall.y = 3
golf.mainBall.sprite = "B"
golf.mainBall.weight = 1

print(golf.calcAirTime(3, 20, -9.8, 20))