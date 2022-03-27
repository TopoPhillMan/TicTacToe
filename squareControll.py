

class boardSquare:
    value = "-"

class rowX:
    y = []

class board:
    x = []

mainBoard = board()

def makeBoard():
    for a in range(3):
        mainBoard.x.append(rowX)
        for b in range(3):
            mainBoard.x[a].y.append("-")

def changeSqare(x,y,changeTo):
    if x == "a":
        x = 0
    elif x == "b":
        x = 1
    elif x == "c":
        x = 2
    else: 
        print("ERROR: Unknown x value")
        
    mainBoard.x[x].y[y] = changeTo

makeBoard()
changeSqare("a",0,"x")
print(mainBoard.x[0].y[0])

