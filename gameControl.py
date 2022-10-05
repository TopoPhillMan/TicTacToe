import squareControl as sC
import gameControl as gC
import ticFunctions as tic
import connectFunctions as con

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

def play():
    print("""
What Game do you want to play
1. TicTackToe
2. Connect 4""")
    gameChoice = int(input("> "))
    if gameChoice == 1:
        print("""
What game style would you like to use?
1. Clasic: 3x3 Board, Win Length 3
2. Large: 5x5 board, Win Length 5
3. Weird: 5x5 board, Win length 3
4. Custom
        """)
        gameStyleChoice = int(input("> "))
        if gameStyleChoice == 1:
            gC.clearScreen()
            tic.ticTackToeMainLoop(3,3,3)
        if gameStyleChoice == 2:
            gC.clearScreen()
            tic.ticTackToeMainLoop(5,5,5)
        if gameStyleChoice == 3:
            gC.clearScreen()
            tic.ticTackToeMainLoop(5,5,3)
        if gameStyleChoice == 4:
            tic.ticTackToeMainLoop(int(input("How Wide is the Board\n > ")),int(input("How Tall is the Board\n > ")),int(input("How Long to Win\n > ")))
    elif gameChoice == 2:
        gC.clearScreen()
        print("""
What game style would you like to use?
1. Clasic: 6x6 Board, Win Length 4
2. Large: 10x10 board, Win Length 5
3. Weird: 4x4 board, Win length 3
4. Custom
        """)
        gameStyleChoice = int(input("> "))
        if gameStyleChoice == 1:
            gC.clearScreen()
            con.connectFourMainLoop(6,6,4)
        if gameStyleChoice == 2:
            gC.clearScreen()
            con.connectFourMainLoop(10,10,5)
        if gameStyleChoice == 3:
            gC.clearScreen()
            con.connectFourMainLoop(4,4,3)
        if gameStyleChoice == 4:
            con.connectFourMainLoop(int(input("How Wide is the Board\n > ")),int(input("How Tall is the Board\n > ")),int(input("How Long to Win\n > ")))
    else:
        print("Invalid Input")


        