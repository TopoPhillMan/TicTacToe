import squareControll as sC

def printScreen(turn,turnNumber):
    player = ""
    if turn == 0:
        player = "X"
    elif turn == 1:
        player = "O"
    else:
        print ("ERROR: Invalid Player Turn")

    print(f"Turn {turnNumber} - {player} Move")
    sC.printBoard

def processInputX(input):
    xRaw = input[0:1]

    x = ""

    if xRaw == "a":
        x = 1
    elif xRaw == "b":
        x = 2
    elif xRaw == "c":
        x = 3
    else:
        print("ERROR: Invalid Input")

    return x

def processInputY(input):
    yRaw = input[1:2]

    y = ""

    if yRaw == "1":
        y = 1
    elif yRaw == "2":
        y = 2
    elif yRaw == "3":
        y = 3
    else:
        print("ERROR: Invalid Input")

    return y

def checkWin(checkFor):
    if sC.mainBoard.x[0].y[0] == checkFor and  sC.mainBoard.x[0].y[1] == checkFor and  sC.mainBoard.x[0].y[2] == checkFor:
        return 1
    if sC.mainBoard.x[1].y[0] == checkFor and  sC.mainBoard.x[1].y[1] == checkFor and  sC.mainBoard.x[1].y[2] == checkFor:
        return 1
    if sC.mainBoard.x[2].y[0] == checkFor and  sC.mainBoard.x[2].y[1] == checkFor and  sC.mainBoard.x[2].y[2] == checkFor:
        return 1
    if sC.mainBoard.x[0].y[0] == checkFor and  sC.mainBoard.x[1].y[0] == checkFor and  sC.mainBoard.x[2].y[0] == checkFor:
        return 1
    if sC.mainBoard.x[0].y[1] == checkFor and  sC.mainBoard.x[1].y[1] == checkFor and  sC.mainBoard.x[2].y[1] == checkFor:
        return 1
    if sC.mainBoard.x[0].y[2] == checkFor and  sC.mainBoard.x[1].y[2] == checkFor and  sC.mainBoard.x[2].y[2] == checkFor:
        return 1
    if sC.mainBoard.x[0].y[0] == checkFor and  sC.mainBoard.x[1].y[1] == checkFor and  sC.mainBoard.x[2].y[2] == checkFor:
        return 1
    if sC.mainBoard.x[0].y[2] == checkFor and  sC.mainBoard.x[1].y[1] == checkFor and  sC.mainBoard.x[2].y[0] == checkFor:
        return 1
    

