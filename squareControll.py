
class rowX:
    y = []

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


def printBoard():
    print(f"{mainBoard.x[0].y[0]} | {mainBoard.x[1].y[0]} | {mainBoard.x[2].y[0]}")
    print("──┼───┼──")
    print(f"{mainBoard.x[0].y[1]} | {mainBoard.x[1].y[1]} | {mainBoard.x[2].y[1]}")
    print("──┼───┼──")
    print(f"{mainBoard.x[0].y[2]} | {mainBoard.x[1].y[2]} | {mainBoard.x[2].y[2]}")

def changeSquare(x,y,changeTo):
    mainBoard.x[x].y[y] = changeTo

def checkSquareFilled(x,y):
    if mainBoard.x[x].y[y] != "-":
        