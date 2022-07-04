import squareControl as sC
import gameControl as gC
import testing as test

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

# TicTackToe

def ticTackToeMainLoop(xRows, yRows, winLength):
    winCondition = True
    currentTurn = "X"
    turnNumber = 1
    sC.mainBoard.x = sC.board.genBoard(xRows, yRows)
    sC.mainBoard.xRows = xRows
    sC.mainBoard.yRows = yRows

    while winCondition:
        if checkBoardFilled():
            resetGame()
            return None
        printScreen(currentTurn,turnNumber)
        mainInputXRaw = int(input("X Position> "))
        mainInputYRaw = int(input("Y Position> "))
        mainInputX = mainInputXRaw - 1
        mainInputY = mainInputYRaw - 1
        if sC.checkSquareFilled(mainInputX,mainInputY):
            continue
        sC.mainBoard.x[mainInputX][mainInputY] = currentTurn
        if checkWin(currentTurn, winLength, xRows, yRows):
            clearScreen()
            displayWin(currentTurn)
            gC.gameContinues = False
            break
        if currentTurn == "X":
            currentTurn = "O"
        elif currentTurn == "O":
            currentTurn = "X"
        turnNumber += 1
        clearScreen()

# Connect4

def findHighestUnfilled(row, yRows):
    for x in range(yRows):
        if sC.mainBoard.x[row][x] != " ":
            continue
        else:
            return x

def collumFull(row, yRows):
    if sC.mainBoard.x[row][yRows-1] != " ":
        return True
    else:
        return False



def connectFourMainLoop(xRows, yRows, winLength):
    winCondition = True
    currentTurn = "X"
    turnNumber = 1
    sC.mainBoard.x = sC.board.genBoard(xRows, yRows)
    sC.mainBoard.xRows = xRows
    sC.mainBoard.yRows = yRows
    while winCondition:
        if checkBoardFilled():
            resetGame()
            return None
        printScreen(currentTurn,turnNumber)
        mainInputXRaw = int(input("What Collum Do You Want To Place Into> "))
        mainInputX = mainInputXRaw - 1
        if collumFull(mainInputX, yRows):
            clearScreen()
            print("That Collum is Full!")
            turnNumber -= 1
            continue
        sC.mainBoard.x[mainInputX][findHighestUnfilled(mainInputX, yRows)] = currentTurn
        if checkWin(currentTurn, winLength, xRows, yRows):
            clearScreen()
            displayWin(currentTurn)
            gC.gameContinues = False
            break
        if currentTurn == "X":
            currentTurn = "O"
        elif currentTurn == "O":
            currentTurn = "X"
        turnNumber += 1
        clearScreen()



        