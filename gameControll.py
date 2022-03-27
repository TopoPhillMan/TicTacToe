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



