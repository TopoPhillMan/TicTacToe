import gameControll as gC
import squareControll as sC

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
        print(playerIcon)
        sC.mainBoard.x[mainInputX][mainInputY] = playerIcon
        checkWinCondition = gC.checkWin(currentTurn)
        if checkWinCondition:
            print(f"{playerIcon} WINS!")
            break
        if currentTurn == 0:
            currentTurn = 1
        elif currentTurn == 1:
            currentTurn = 0
        turnNumber += 1
        gC.clearScreen()

mainLoop()