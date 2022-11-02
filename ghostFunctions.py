import gameControl as gC
import squareControl as sC
import ghostFunctions as gho
from msvcrt import getch
from random import random

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
    gho.mazeMap = sC.board.genBoard(xLines*3,yLines*3)
    gho.charcterMap = sC.board.genBoard(xLines*3,yLines*3)
    gho.wallMap = mazeStackCell.genBoard(xLines,yLines)


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
            gho.charcterMap[startY+y][startX+x] = cluster[y][x]

class mazeStackCell():
    def __init__(self, visited, x, y):
        self.self = self
        self.visited = visited
        self.x = x 
        self.y = y
    north = True
    south = True 
    east = True
    west = True

    def genBoard(xLine, yLine):
        boardTemp = []
        for x in range(xLine):
            boardTemp.insert(xLine, [])
    
        for x in range(xLine):
            for y in range(yLine):
                boardTemp[x].append(mazeStackCell(False,x,y))
        return boardTemp
    
    def checkDeadEnd(self):
        xLine = self.x
        yLine = self.y

        tracker = 0
        if yLine - 1 >= 0:
            if wallMap[xLine][yLine-1].visited == True:
                tracker += 1
        else: 
            tracker += 1

        if yLine + 1 <= len(gho.wallMap[0]):
            if wallMap[xLine][yLine+1].visited == True:
                tracker += 1
        else: 
            tracker += 1
        
        if xLine +1 <= len(gho.wallMap):
            if wallMap[xLine+1][yLine].visited == True:
                tracker += 1
        else: 
            tracker += 1

        if xLine -1 >= 0:
            if wallMap[xLine-1][yLine].visited == True:
                tracker += 1
        else:
            tracker += 1
        
        if tracker == 4:
            return True
        else:
            return False
        
    def chooseJunction(self):

        xLine = self.x
        yLine = self.y
        while True:
            ran = random()
            if ran >= 0 and ran < 0.25 and yLine - 1 >= 0:
                if wallMap[xLine-0][yLine-1].visited == False:
                    return 'north'
            elif ran >= 0.25 and ran < 0.5 and yLine + 1 <= len(gho.wallMap[0]):
                if wallMap[xLine][yLine+1].visited == False:
                    return 'south'
            elif ran >= 0.5 and ran < 0.75 and xLine +1 <= len(gho.wallMap):
                if wallMap[xLine+1][yLine].visited == False:
                    return 'east'
            elif ran >= 0.75 and ran <= 1 and xLine -1 >= 0:
                if wallMap[xLine-1][yLine].visited == False:
                    return 'west'
            
    def addToPath(x,y):
        mainStackPath.append((x,y))
    
    def backTrack():
        del mainStackPath[-1]
    
    def goDirection(self,direction):
        if direction == 'north':
            self.north = False
            return (self.x,self.y-1)
        elif direction == 'south':
            self.south = False
            return (self.x,self.y+1)
        elif direction == 'east':
            self.east = False
            return (self.x+1,self.y)
        elif direction == 'west':
            self.west = False
            return (self.x-1,self.y)
    
    def makeMaze(self):
        mazeStackCell.addToPath(0,0)
        while (wallMap[0][0].checkDeadEnd() != True):
            currentX = mainStackPath[-1][0]
            currentY = mainStackPath[-1][1]

            if wallMap[currentX][currentY].checkDeadEnd():
                mazeStackCell.backTrack()
                continue
            else:
                cords = wallMap[currentX][currentY].goDirection(wallMap[currentX][currentY].chooseJunction())
                mazeStackCell.addToPath(cords[0], cords[1])




wallMap = gho.mazeStackCell
mainStackPath = []




