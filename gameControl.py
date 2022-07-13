import squareControl as sC
import gameControl as gC

gameContinues = True

# General Controls

def printScreen(turn,turnNumber):

    print(f" Turn {turnNumber} - {turn} Move")
    sC.printBoardSeperated(sC.mainBoard.xRows, sC.mainBoard.yRows)
    print("")

def checkWin(turn, length, xRows, yRows):

    # Vertical
    for x in range(xRows):
        for z in range(yRows - (length - 1)):
            checkTally = 0
            for y in range(length):
                if sC.mainBoard.x[x][z+y] == turn:
                    checkTally += 1
            if checkTally == length:
                return True

    # Horizontal
    for y in range(yRows):
        for z in range(xRows - (length - 1)):
            checkTally = 0
            for x in range(length):
                if sC.mainBoard.x[z+x][y] == turn:
                    checkTally += 1
            if checkTally == length:
                return True

    # Diagnal
    for x in range(xRows - (length-1)):
        for y in range(yRows):
            checkTallyD = 0
            checkTallyU = 0
            for z in range(length):
                if sC.mainBoard.x[x+z][x-z] == turn:
                    checkTallyD += 1
                if sC.mainBoard.x[x+z][x+z] == turn:
                    checkTallyU += 1
            if checkTallyD == length or checkTallyU == length:
                return True

    return False
        
def clearScreen():
    counter = 0
    while counter < 100: 
        print("")
        counter += 1
        
def displayWin(playerIcon):
    print("-------")
    print(f"{playerIcon} WINS!")
    print("-------")
    print("")
    gC.gameContinues = False

def checkBoardFilled():
    xRows = sC.mainBoard.xRows
    yRows = sC.mainBoard.yRows
    check = 0
    for x in range(xRows):
        for y in range(yRows):
            if sC.mainBoard.x[x][y] != " ":
                check += 1
    if check == xRows * yRows:
        return True
    else:
        return False

def resetGame():
    xRows = sC.mainBoard.xRows
    yRows = sC.mainBoard.yRows
    for x in range(xRows):
        for y in range(yRows):
            sC.mainBoard.x[x][y] = " "




        