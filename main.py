import gameControl as gC
import squareControl as sC
import testing as test

gC.connectFourMainLoop(6,6,4)

# while gC.gameContinues:
#   gC.connectFourMainLoop(6,6,4)
#   print("Game Restarting due to Full Board")

# sC.mainBoard.xRows = 6
# sC.mainBoard.yRows = 6
# sC.mainBoard.x = sC.board.genBoard(sC.mainBoard.xRows, sC.mainBoard.yRows)
# sC.mainBoard.x[0][0] = "X"
# sC.mainBoard.x[0][1] = "X"
# sC.mainBoard.x[0][2] = "X"
# sC.mainBoard.x[0][3] = "X"
# sC.printBoardSeperated(sC.mainBoard.yRows, sC.mainBoard.xRows)
# print(gC.collumFull(0,sC.mainBoard.yRows))