import gameControl as gC
import squareControl as sC
import connectFunctions as con

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

def checkBounds(xInput):
    if xInput >= sC.mainBoard.xRows:
        return True
    elif xInput < 0:
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
        if gC.checkBoardFilled():
            gC.resetGame()
            return None
        gC.printScreen(currentTurn,turnNumber)
        mainInputXRaw = int(input("What Collum Do You Want To Place Into> "))
        mainInputX = mainInputXRaw - 1
        if con.checkBounds(mainInputX):
            gC.clearScreen()
            print("Out of Bounds!")
            continue
        if con.collumFull(mainInputX, yRows):
            gC.clearScreen()
            print("That Collum is Full!")
            continue
        sC.mainBoard.x[mainInputX][con.findHighestUnfilled(mainInputX, yRows)] = currentTurn
        if gC.checkWin(currentTurn, winLength, xRows, yRows):
            gC.clearScreen()
            gC.displayWin(currentTurn)
            gC.gameContinues = False
            break
        if currentTurn == "X":
            currentTurn = "O"
        elif currentTurn == "O":
            currentTurn = "X"
        turnNumber += 1
        gC.clearScreen()