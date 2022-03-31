import gameControll as gC
import squareControll as sC

def mainLoop():
    winCondition = True
    currentTurn = 0
    playerIcon = "X"
    turnNumber = 1
    while winCondition:
        gC.printScreen(currentTurn,turnNumber)
        mainInputX = int(input("X Position> "))
        mainInputY = int(input("Y Position> "))
        gC.checkInvalidInput(mainInputX,mainInputY)
        if sC.checkSquareFilled(mainInputX,mainInputY):
            continue
        if currentTurn == 0:
            playerIcon = "X"
        elif currentTurn == 1:
            playerIcon = "O"
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

mainLoop()