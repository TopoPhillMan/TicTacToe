import squareControl as sC
import gameControl as gC
import testing as test

gameContinues = True

def printScreen(turn,turnNumber):

    print(f" Turn {turnNumber} - {turn} Move")
    sC.printBoard(sC.mainBoard.xRows, sC.mainBoard.yRows)
    print("")

# def checkInput(n):
#     if n == 1:
#         return False
#     elif n == 2:
#         return False
#     elif n == 3:
#         return False
#     else:
#         return True

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

    # if turn == 0:
    #     checkFor = "X"
    # elif turn == 1:
    #     checkFor = "O"
    # else:
    #     print ("ERROR: Invalid Player Turn")

    # if sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[1][0] == checkFor and sC.mainBoard.x[2][0] == checkFor:
    #     return True
    # elif sC.mainBoard.x[0][1] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[2][1] == checkFor:
    #     return True
    # elif sC.mainBoard.x[0][2] == checkFor and sC.mainBoard.x[1][2] == checkFor and sC.mainBoard.x[2][2] == checkFor:
    #     return True
    # elif sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[0][1] == checkFor and sC.mainBoard.x[0][2] == checkFor:
    #     return True
    # elif sC.mainBoard.x[1][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[1][2] == checkFor:
    #     return True
    # elif sC.mainBoard.x[2][0] == checkFor and sC.mainBoard.x[2][1] == checkFor and sC.mainBoard.x[2][2] == checkFor:
    #     return True
    # elif sC.mainBoard.x[0][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[2][2] == checkFor:
    #     return True
    # elif sC.mainBoard.x[2][0] == checkFor and sC.mainBoard.x[1][1] == checkFor and sC.mainBoard.x[0][2] == checkFor:
    #     return True
    # else:
    #     return False 
        
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
            if sC.mainBoard.x[x][y] != "⠀":
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
            sC.mainBoard.x[x][y] = "⠀"

def mainLoop(xRows, yRows, winLength):
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
        # if checkInput(mainInputX) == True  or checkInput(mainInputY):
        #     print("ERORR: Invalid Input")
        #     continue
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



