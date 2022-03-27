

class boardSquare:
    value = "-"

class rowX:
    y = []
class row:
    y0 = ""
    y1 = ""
    y2 = ""

class board:
    x = [rowX,rowX,rowX]
    
    def __getitem__(self, i):
        return f"Value {i}"

mainBoard = board()

def makeBoard():
    for a in range(3):
        mainBoard.x.append(rowX)
        for b in range(3):
            mainBoard.x[a].y.append("-")

def changeSqare(x,y,changeTo):
    if x == "a":
        x = 0
        x = "0"
    elif x == "b":
        x = 1
        x = "1"
    elif x == "c":
        x = 2
        x = "2"
    else: 
        print("ERROR: Unknown x value")
        
    mainBoard.x[x].y[y] = changeTo
    mainBoard.x[x[y]] = changeTo

def printBoard():
    print(f"{mainBoard.x[0].y[0]} | {mainBoard.x[1].y[0]} | {mainBoard.x[2].y[0]}")
    print("──┼──┼──")
    print(f"{mainBoard.x[0].y[1]} | {mainBoard.x[1].y[1]} | {mainBoard.x[2].y[1]}")
    print("──┼──┼──")
    print(f"{mainBoard.x[0].y[2]} | {mainBoard.x[1].y[2]} | {mainBoard.x[2].y[2]}")


makeBoard()
printBoard()

changeSqare("a",0,"x")
print(mainBoard.x[0].y[0])
