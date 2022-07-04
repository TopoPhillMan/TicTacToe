import gameControl as gC
import squareControl as sC
import ticFunctions as tic
import connectFunctions as con

def play():
    print("""
    What Game do you want to play
    1. TicTackToe
    2. Connect 4""")
    gameChoice = int(input("> "))
    if gameChoice == 1:
        tic.ticTackToeMainLoop(3,3,3)
    elif gameChoice == 2:
        con.connectFourMainLoop(6,6,4)
    else:
        print("Invalid Input")

play()


# gC.connectFourMainLoop(6,6,4)

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