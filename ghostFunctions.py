import gameControl as gC
import squareControl as sC
import ghostFunctions as gho
from msvcrt import getch

# Layer entrance - ⛶
# Player character - ⚇

# ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ 
# ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟
# ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯
# ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ 
# ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ 
# ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ 
# ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ 

mazeMap = []
charcterMap = []
def printBoard(xLines, yLines):
    outputString = ""
    for x in range(xLines):
        for y in range(yLines):
            outputString += sC.mainBoard.x[x][y]
        outputString += "\n"
    print(outputString)

def biuldMap(xLines, yLines):
    gho.mazeMap = sC.board.genBoard(xLines,yLines)
    gho.charcterMap = sC.board.genBoard(xLines,yLines)


class cluster():
    class straight():
        vertical = [["│"," ","│"]]
        horizontal = [["─"],[" "],["─"]]
    class turn():
        class up():
            right = [["┌","─","─"],["│"," "," "],["│","","┌"]]
            left = [["─","─","┐"],[" "," ","│"],["┐","","│"]]
        class down(): 
            left = [["└","─","─"],["│","",""],["│","","└"]]
            right = [["─","─","┘"],["","","│"],["┘","","│"]]
    class loop():
        up = [["┌","─","─","─","┐"],["│"," "," "," ","│"],["│"," ","│"," ","│"]]
        down = [["│"," ","│"," ","│"],["│"," "," "," ","│"],["└","─","─","─","┘"]]
        right = [["┌","─","─"],["│"," "," "],["│"," ","─"],["│"," "," "],["└","─","─"]]
        left = [["─","─","┐"],[" "," ","│"],["─"," ","│"],[" "," ","│"],["─","─","┘"]]

def biuldCluster(inputArray):
    outputerCluster = sC.board.genBoard(len(inputArray[0]),len(inputArray))
    for x in range(len(inputArray[0])):
        for y in range(len(inputArray)):
            outputerCluster[x][y] = inputArray[y][x]
    return outputerCluster

def addCluster(cluster,startX,startY):
    xLength = len(cluster[0])
    yLength = len(cluster)

    for y in range(yLength):
        for x in range(xLength):
            gho.mazeMap[startY+y][startX+x] = cluster[y][x]


 