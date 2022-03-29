import gameControll as gC
import squareControll as sC

def mainLoop():
    winCondition = True
    currentTurn = 0
    while winCondition:
        gC.printScreen()
        mainInput = input("> ")
        xInput = gC.processInputX(mainInput)
        yInput = gC.processInputY(mainInput)
        if sC.checkSquareFilled(xInput,yInput):
            return
        if currentTurn