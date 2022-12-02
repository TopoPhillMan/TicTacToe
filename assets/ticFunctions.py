import controllers.gameControl as gC
import controllers.squareControl as sC
import assets.ticFunctions as tic

def checkBounds(xInput, yInput):
    if xInput >= sC.mainBoard.xRows:
        return True
    elif xInput < 0:
        return True
    elif yInput >= sC.mainBoard.yRows:
        return True
    elif yInput < 0:
        return True
    else: 
        return False

def ticTackToeMainLoop(xRows, yRows, winLength):
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
        mainInputXRaw = int(input("X Position> "))
        mainInputYRaw = int(input("Y Position> "))
        mainInputX = mainInputXRaw - 1
        mainInputY = mainInputYRaw - 1
        if tic.checkBounds(mainInputX, mainInputY):
            gC.clearScreen()
            print("Out of Bounds!")
            continue
        if sC.checkSquareFilled(mainInputX,mainInputY):
            continue
        sC.mainBoard.x[mainInputX][mainInputY] = currentTurn
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