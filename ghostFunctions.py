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
    gho.inlineMap = sC.board.genBoard(xLines,yLines)


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

        if yLine + 1 <= len(gho.wallMap[0])-1:
            if wallMap[xLine][yLine+1].visited == True:
                tracker += 1
        else: 
            tracker += 1
        
        if xLine +1 <= len(gho.wallMap)-1:
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
            elif ran >= 0.25 and ran < 0.5 and yLine + 1 <= len(gho.wallMap[0])-1:
                if wallMap[xLine][yLine+1].visited == False:
                    return 'south'
            elif ran >= 0.5 and ran < 0.75 and xLine +1 <= len(gho.wallMap)-1:
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
            return (self.x,self.y-1)
        elif direction == 'south':
            return (self.x,self.y+1)
        elif direction == 'east':
            return (self.x+1,self.y)
        elif direction == 'west':
            return (self.x-1,self.y)

    def removeWalls(self,direction):
        if direction == 'north':
            self.north = False
            wallMap[self.x][self.y-1].south = False
        if direction == 'south':
            self.south = False
            wallMap[self.x][self.y+1].north = False
        if direction == 'east':
            self.east = False
            wallMap[self.x+1][self.y].west = False
        if direction == 'west': 
            self.west = False
            wallMap[self.x-1][self.y].east = False


    
    def makeMaze(self): 

        counter = 0
        junctDrirection = gho.wallMap[0][0].chooseJunction()
        cordsNew = gho.wallMap[0][0].goDirection(junctDrirection)
        mazePath.append((0,0,junctDrirection))
        gho.mazeStackCell.addToPath(0,0)
        gho.wallMap[0][0].visited = True

        while len(gho.mainStackPath) > 0:
            currnetX = cordsNew[0]
            currentY = cordsNew[1]

            if gho.wallMap[currnetX][currentY].checkDeadEnd():
                gho.wallMap[currnetX][currentY].visited = True
                cordsNew = gho.mainStackPath[-1]
                gho.mazeStackCell.backTrack()
            else:
                junctDrirection = gho.wallMap[currnetX][currentY].chooseJunction()
                cordsNew = gho.wallMap[currnetX][currentY].goDirection(junctDrirection)
                mazePath.append((currnetX,currentY,junctDrirection))
                gho.mazeStackCell.addToPath(currnetX,currentY)
                gho.wallMap[currnetX][currentY].visited = True
    
    def removeWalls():
        for i in range(len(mazePath)):
            curentX = mazePath[i][0]
            curentY = mazePath[i][1]
            direction = mazePath[i][2]
            
            if direction == 'north':
                wallMap[curentX][curentY].north = False
                wallMap[curentX][curentY-1].south = False
            
            if direction == 'south':
                wallMap[curentX][curentY].south = False
                wallMap[curentX][curentY+1].north = False
            
            if direction == 'east':
                wallMap[curentX][curentY].east = False
                wallMap[curentX+1][curentY].west = False
            
            if direction == 'west':
                wallMap[curentX][curentY].west = False
                wallMap[curentX-1][curentY].east = False
                
    def generateMapInline():
        for x in range(len(wallMap)):
            for y in range(len(wallMap[0])):
                inlineMap[y*3][x*3] = "█"
                inlineMap[y*3][x*3+2] = "█"
                inlineMap[y*3+1][x*3+1] = " "
                inlineMap[y*3+2][x*3] = "█"
                inlineMap[y*3+2][x*3+2] = "█"

                if wallMap[x][y].north == True:
                    inlineMap[y*3][(x*3)+1] = "█"
                else:
                    inlineMap[y*3][x*3+1] = " "

                if wallMap[x][y].west == True:
                    inlineMap[y*3+1][x*3] = "█"
                else:
                    inlineMap[y*3+1][x*3] = " "

                if wallMap[x][y]. east == True:
                    inlineMap[y*3+1][x*3+2] = "█"
                else:
                    inlineMap[y*3+1][x*3+2] = " "

                if wallMap[x][y].south == True:
                    inlineMap[y*3+2][x*3+1] = "█"
                else:
                    inlineMap[y*3+2][x*3+1] = " "
                

                


                

# ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ 
# ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟
# ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯
# ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ 
# ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ 
# ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ 
# ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ ╭ ╮ ╯ 
# ╰ ╱ ╲ ╳ ╴ ╵ ╶ ╷ ╸ ╹ ╺ ╻ ╼ ╽ ╾ ╿


wallMap = gho.mazeStackCell
inlineMap = gho.mazeStackCell
mainStackPath = []
mazePath = []




