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

def numSpacingCorectionY(yRows, rowNumber):
    outputString = ""
    maxLength = len(f"{yRows}")
    countLength = len(f"{rowNumber}")

    for x in range(maxLength - countLength):
        outputString += "0"
    
    outputString += str(rowNumber)
    
    return(outputString)

def yNumSpacer(yRows):
    outputString = ""
    for x in range(len(str(yRows))):
        outputString+="┄"
    return outputString

def numSpacingCorrectionX(xRows):
    outputString = ""
    baseRowLeadin = numSpacingCorectionY(sC.mainBoard.yRows, "  ") + " ┆ "
    
    for x in range(len(str(xRows))):
        if x == 0:
            for x in range(len(numSpacingCorectionY(sC.mainBoard.yRows, "*"))-1):
                outputString += " "
            outputString += "  ┆ "
        else:
            outputString += baseRowLeadin
        for y in range(xRows):
            splitNumber = list(str(y+1))
            delayTimes = len(str(xRows)) - len(splitNumber)
            if delayTimes >= (x+1):
                outputString += "0" 
            else:
                outputString += splitNumber[x-delayTimes]
            outputString += " ┆ "
        outputString += "\n"
    
    return outputString

def printBoardCombined(yRows, xRows):
    outputString = ""

    outputString += " ┌"
    for x in range(xRows):
        outputString += "─"
    outputString += "┐\n"

    for y in range(yRows):
        outputString += f" |"
        for x in range(xRows):
            outputString += mainBoard.x[x][(yRows-1) - y]
        outputString += f"|\n"


    outputString += f" └"
    for x in range(xRows):
        outputString += "─"
    outputString += f"┘\n"
    
    print(outputString)

def printBoardSeperated(yRows, xRows):
    ySpacer = yNumSpacer(yRows)
    outputString = ""

    # Top Cap
    for x in range(len(numSpacingCorectionY(sC.mainBoard.yRows, "*"))-1):
        outputString += " "
    outputString += "  ┌"
    for x in range(xRows-1):
        outputString += "───┬"
    outputString += "───┐\n"

    # Middsection
    for y in range(yRows-1):
        outputString += sC.numSpacingCorectionY(yRows, yRows- y)
        for x in range(xRows):
            outputString += " | "
            outputString += mainBoard.x[x][(yRows-1) - y]
        outputString += f" | \n{ySpacer}┄├"
        for x in range(xRows-1):
            outputString += "───┼"
        outputString += "───┤\n"

    outputString += sC.numSpacingCorectionY(yRows, 1)
    for x in range(xRows):
        outputString += " | "
        outputString += mainBoard.x[x][(yRows-1) - (yRows-1)]
    outputString += " |\n"

    # Bottom Cap
    outputString += f"{ySpacer}┄└"
    for x in range(xRows-1):
        outputString += "───┴"
    outputString += f"───┘\n{numSpacingCorrectionX(sC.mainBoard.xRows)}"
    
    print(outputString)

def checkSquareFilled(x,y):
    if mainBoard.x[x][y] != " ":
        print("ERROR: Square Already Occupied")
        return True
    else:
        return False
