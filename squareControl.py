import squareControl as sC

class board:
    
    def __init__(self):
        pass
    
    x = []
    
    def genBoard(xLine, yLine):
        lineInternal = []
        boardTemp = []
        for y in range(yLine):
            lineInternal.append("")
        for x in range(xLine):
            boardTemp.append(lineInternal)
        return boardTemp

    def __getitem__(self, i):
        return f"Value {i}"

mainBoard = board()

def printBoard():

    print(f"   ┌───────────┐")
    print(f" 3 | {mainBoard.x[0][2]} | {mainBoard.x[1][2]} | {mainBoard.x[2][2]} |")
    print("   | ──┼───┼── |")
    print(f" 2 | {mainBoard.x[0][1]} | {mainBoard.x[1][1]} | {mainBoard.x[2][1]} |")
    print("   | ──┼───┼── |")
    print(f" 1 | {mainBoard.x[0][0]} | {mainBoard.x[1][0]} | {mainBoard.x[2][0]} |")
    print("   └───────────┘")
    print(" *   1   2   3  ")


def changeSquare(x,y,changeTo):
    mainBoard.x[x][y] = changeTo

def checkSquareFilled(x,y):
    if mainBoard.x[x][y] != "-":
        print("ERROR: Square Already Occupied")
        return True
    else:
        return False
