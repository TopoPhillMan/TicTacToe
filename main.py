import gameControll as gC
import squareControll as sC
import testing as test

def mainLoop():
    winCondition = True
    currentTurn = 0
    playerIcon = "X"
    turnNumber = 1
    while winCondition:

        gC.printScreen(currentTurn,turnNumber)
        mainInputXRaw = int(input("X Position> "))
        mainInputYRaw = int(input("Y Position> "))
        mainInputX = mainInputXRaw - 1
        mainInputY = mainInputYRaw - 1
        gC.checkInvalidInput(mainInputX,mainInputY)
        if sC.checkSquareFilled(mainInputX,mainInputY):
            continue
        sC.mainBoard.x[mainInputX][mainInputY] = playerIcon
        if gC.checkWin(currentTurn):
            gC.clearScreen()
            gC.displayWin(playerIcon)
            break
        if currentTurn == 0:
            currentTurn = 1
            playerIcon = "O"
        elif currentTurn == 1:
            currentTurn = 0
            playerIcon = "X"
        turnNumber += 1
        gC.clearScreen()

test.checkWin(1,"X")
sC.printBoard()