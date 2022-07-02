from calendar import c
from numpy import outer
import squareControl as sC

class board:
    x = []
    xRows = int
    yRows = int

    def genBoard(xLine, yLine):
        boardTemp = []
        for x in range(xLine):
            boardTemp.insert(xLine, [])
        
        for x in range(xLine):
           for y in range(yLine):
                boardTemp[x].append(" ")

        return boardTemp

mainBoard = board()

def numSpaceingCorectionY(yRows, rowNumber):
    outputString = f"{rowNumber}"
    maxLength = len(f"{yRows}")
    countLength = len(f"{rowNumber}")

    for x in range(maxLength - countLength):
        outputString += " "
    
    return(outputString)



def printBoardSeperated(yRows, xRows):
    outputString = ""
    blank = " "

    # Top Cap
    outputString += "  ┌"
    for x in range(xRows-1):
        outputString += "───┬"
    outputString += "───┐\n"

    # Middsection
    for y in range(yRows-1):
        outputString += sC.numSpaceingCorectionY(yRows, yRows- y)
        for x in range(xRows):
            outputString += " | "
            outputString += mainBoard.x[x][(yRows-1) - y]
        outputString += f" | \n{sC.numSpaceingCorectionY(yRows, blank)} ├"
        for x in range(xRows-1):
            outputString += "───┼"
        outputString += "───┤\n"

    outputString += sC.numSpaceingCorectionY(yRows, 1)
    for x in range(xRows):
        outputString += " | "
        outputString += mainBoard.x[x][(yRows-1) - (yRows-1)]
    outputString += " |\n"

    # Bottom Cap
    outputString += f"{sC.numSpaceingCorectionY(yRows, blank)} └"
    for x in range(xRows-1):
        outputString += "───┴"
    outputString += "───┘\n* "
    for x in range(xRows):
        outputString += "  "
        outputString += str(x + 1)
        outputString += " "

    print(outputString)

def printBoardComined(yRows, xRows):
    outputString = ""

    # Top Cap
    outputString += "  ┌"
    for x in range(xRows-1):
        outputString += "─"
    outputString += "─┐\n"

    # Middsection
    for y in range(yRows-1):
        outputString += str(yRows- y)
        for x in range(xRows):
            outputString += " | "
            outputString += mainBoard.x[x][(yRows-1) - y]
        outputString += " | \n  ├"
        for x in range(xRows-1):
            outputString += "───┼"
        outputString += "───┤\n"

    outputString += str(yRows - (yRows - 1))
    for x in range(xRows):
        outputString += " | "
        outputString += mainBoard.x[x][(yRows-1) - (yRows-1)]
    outputString += " |\n"

    print(outputString)


    # print(f"   ┌───────────┐")
    # print(f" 3 | {mainBoard.x[0][2]} | {mainBoard.x[1][2]} | {mainBoard.x[2][2]} |")
    # print("   | ──┼───┼── |")
    # print(f" 2 | {mainBoard.x[0][1]} | {mainBoard.x[1][1]} | {mainBoard.x[2][1]} |")
    # print("   | ──┼───┼── |")
    # print(f" 1 | {mainBoard.x[0][0]} | {mainBoard.x[1][0]} | {mainBoard.x[2][0]} |")
    # print("   └───────────┘")
    # print(" *   1   2   3  ")

def checkSquareFilled(x,y):
    if mainBoard.x[x][y] != " ":
        print("ERROR: Square Already Occupied")
        return True
    else:
        return False
