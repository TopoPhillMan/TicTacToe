import squareControll as sC
import testing as test

gameContinues = True

def printScreen(turn,turnNumber):
    player = ""
    if turn == 0:
        player = "X"
    elif turn == 1:
        player = "O"
    else:
        print ("ERROR: Invalid Player Turn")

    print(f" Turn {turnNumber} - {player} Move")
    sC.printBoard()
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
        
def displayWin(playerIcon):
    print("-------")
    print(f"{playerIcon} WINS!")
    print("-------")
    print("")
    gameContinues = False

def checkGameConplete():
    check = 0
    for x in range(3):
        for y in range(3):
            if sC.mainBoard.x[x][y] != "-":
                check += 1
    if check == 9:
        return True
    else:
        return False

def resetGame():
    for x in range(3):
        for y in range(3):
            sC.mainBoard.x[x][y] = "-"

def mainLoop():
    winCondition = True
    currentTurn = 0
    playerIcon = "X"
    turnNumber = 1
    while winCondition:
        if checkGameConplete():
            resetGame()
            gameContinues = False
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
        sC.mainBoard.x[mainInputX][mainInputY] = playerIcon
        if checkWin(currentTurn):
            clearScreen()
            displayWin(playerIcon)
            break
        if currentTurn == 0:
            currentTurn = 1
            playerIcon = "O"
        elif currentTurn == 1:
            currentTurn = 0
            playerIcon = "X"
        turnNumber += 1
        clearScreen()


