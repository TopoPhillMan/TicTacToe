class row:
    y0 = ""
    y1 = ""
    y2 = ""

class board:
    x = [row,row,row]
    
    def __getitem__(self, i):
        return f"Value {i}"

mainBoard = board()

def changeSqare(x,y,changeTo):
    if x == "a":
        x = "0"
    elif x == "b":
        x = "1"
    elif x == "c":
        x = "2"
    else: 
        print("ERROR: Unknown x value")
        
    mainBoard.x[x[y]] = changeTo

def printBoard():
    print(f"{mainBoard.x[0].y0} | {mainBoard.x[1].y0} | {mainBoard[2].y0}")
    print("──┼──┼──")
    print(f"{mainBoard.x[0].y1} | {mainBoard.x[1].y1} | {mainBoard[2].y1}")
    print("──┼──┼──")
    print(f"{mainBoard.x[0].y2} | {mainBoard.x[1].y2} | {mainBoard[2].y2}")


printBoard()


