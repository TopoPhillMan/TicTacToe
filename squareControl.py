import squareControl as sC

class square:
    value = "⠀"

class line:
    y = []

def createLine(length):
    linePre = line()
    for x in range(length):
        linePre.y.append("⠀")
    return linePre


class board:

    x = []

    def genBoard(xLine, yLine):
        boardTemp = []
        for x in range(xLine):
            boardTemp.insert(xLine, [])
        
        for x in range(xLine):
           for y in range(yLine):
                boardTemp[x].append("⠀")

        return boardTemp

mainBoard = board()

def printBoard(yRows, xRows):
    outputString = ""

    # Top Cap
    outputString += "  ┌"
    for x in range(xRows-1):
        outputString += "───┬"
    outputString += "───┐\n"

    # Middsection
    for y in range(yRows-1):
        outputString += str(y+1)
        for x in range(xRows):
            outputString += " | "
            outputString += mainBoard.x[y][x]
        outputString += " | \n  ├"
        for x in range(xRows-1):
            outputString += "───┼"
        outputString += "───┤\n"

    outputString += str(yRows)
    for x in range(xRows):
        outputString += " | "
        outputString += mainBoard.x[yRows-1][x]
    outputString += " |\n"

    # Bottom Cap
    outputString += "  └"
    for x in range(xRows-1):
        outputString += "───┴"
    outputString += "───┘\n* "
    for x in range(xRows):
        outputString += "  "
        outputString += str(x)
        outputString += " "

    print(outputString)


    # print(f"   ┌───────────┐")
    # print(f" 3 | {mainBoard.x[0][2]} | {mainBoard.x[1][2]} | {mainBoard.x[2][2]} |")
    # print("   | ──┼───┼── |")
    # print(f" 2 | {mainBoard.x[0][1]} | {mainBoard.x[1][1]} | {mainBoard.x[2][1]} |")
    # print("   | ──┼───┼── |")
    # print(f" 1 | {mainBoard.x[0][0]} | {mainBoard.x[1][0]} | {mainBoard.x[2][0]} |")
    # print("   └───────────┘")
    # print(" *   1   2   3  ")


def changeSquare(x,y,changeTo):
    mainBoard.x[x][y] = changeTo

def checkSquareFilled(x,y):
    if mainBoard.x[x][y] != "-":
        print("ERROR: Square Already Occupied")
        return True
    else:
        return False
