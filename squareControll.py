class row:
    y0 = "-"
    y1 = "-"
    y2 = "-"

class board:
    x0 = row()
    x1 = row()
    x2 = row()
    
    def __getitem__(self, i):
        return f"Value {i}"

# There are propably better ways of making dimensional "arrays", but I dont know how to do that

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
    print(f"{mainBoard.x0.y0} | {mainBoard.x1.y0} | {mainBoard.x2.y0}")
    print("──┼───┼──")
    print(f"{mainBoard.x0.y1} | {mainBoard.x1.y1} | {mainBoard.x2.y1}")
    print("──┼───┼──")
    print(f"{mainBoard.x0.y2} | {mainBoard.x1.y2} | {mainBoard.x2.y2}")


printBoard()


