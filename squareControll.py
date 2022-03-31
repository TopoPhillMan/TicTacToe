import squareControll as sC

class board:
    x = [["-","-","-"],["-","-","-"],["-","-","-"]]
    
    # This is a bad way of doing it but I will add a better method using appending latter

    def __getitem__(self, i):
        return f"Value {i}"

mainBoard = board()

def printBoard():
    
    print(f"{mainBoard.x[0][2]} | {mainBoard.x[1][2]} | {mainBoard.x[2][2]}")
    print("──┼───┼──")
    print(f"{mainBoard.x[0][1]} | {mainBoard.x[1][1]} | {mainBoard.x[2][1]}")
    print("──┼───┼──")
    print(f"{mainBoard.x[0][0]} | {mainBoard.x[1][0]} | {mainBoard.x[2][0]}")


def changeSquare(x,y,changeTo):
    mainBoard.x[x][y] = changeTo

def checkSquareFilled(x,y):
    if mainBoard.x[x][y] != "-":
        print("ERROR: Square Already Occupied")
        return True
    else:
        return False
