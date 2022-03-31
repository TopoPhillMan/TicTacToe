from cgi import test
from timeit import repeat
import squareControll as sC

def printScreen(turn,turnNumber):
    player = ""
    if turn == 0:
        player = "X"
    elif turn == 1:
        player = "O"
    else:
        print ("ERROR: Invalid Player Turn")

    print(f"Turn {turnNumber} - {player} Move")
    sC.printBoard()
    print("")


def checkWin(turn):

    if turn == 0:
        checkFor = "X"
    elif turn == 1:
        checkFor = "O"
    else:
        print ("ERROR: Invalid Player Turn")

    if sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[1][0] == checkFor and sC.mainBoard.x[2][0] == checkFor:
        return True
    elif sC.mainBoard.x[0][1] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[2][1] == checkFor:
        return True
    elif sC.mainBoard.x[0][2] == checkFor and sC.mainBoard.x[1][2] == checkFor and sC.mainBoard.x[2][2] == checkFor:
        return True
    elif sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[0][1] == checkFor and sC.mainBoard.x[0][2] == checkFor:
        return True
    elif sC.mainBoard.x[1][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[1][2] == checkFor:
        return True
    elif sC.mainBoard.x[2][0] == checkFor and sC.mainBoard.x[2][1] == checkFor and sC.mainBoard.x[2][2] == checkFor:
        return True
    elif sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[2][2] == checkFor:
        return True
    elif sC.mainBoard.x[2][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[0][2] == checkFor:
        return True
    else:
        return False 
        
        
    
    
def clearScreen():
    counter = 0
    while counter < 100: 
        print("")
        counter += 1

def checkInvalidInput(inputX, inputY):
    if inputX != 1 or inputX != 2 or inputX != 3:
        return True
    if inputY != 1 or inputY != 2 or inputY != 3:
        return True
        
def displayWin(playerIcon):
    print("-------")
    print(f"{playerIcon} WINS!")
    print("-------")
    print("")