import gameControl as gC
import squareControl as sC
import ticFunctions as tic
import connectFunctions as con
import ghostFunctions as gho
from msvcrt import getch

# ─ ━ │ ┃ ┄ ┅ ┆ ┇ ┈ ┉ ┊ ┋ ┌ ┍ ┎ ┏ 
# ┐ ┑ ┒ ┓ └ ┕ ┖ ┗ ┘ ┙ ┚ ┛ ├ ┝ ┞ ┟
# ┠ ┡ ┢ ┣ ┤ ┥ ┦ ┧ ┨ ┩ ┪ ┫ ┬ ┭ ┮ ┯
# ┰ ┱ ┲ ┳ ┴ ┵ ┶ ┷ ┸ ┹ ┺ ┻ ┼ ┽ ┾ ┿ 
# ╀ ╁ ╂ ╃ ╄ ╅ ╆ ╇ ╈ ╉ ╊ ╋ ╌ ╍ ╎ ╏ 
# ═ ║ ╒ ╓ ╔ ╕ ╖ ╗ ╘ ╙ ╚ ╛ ╜ ╝ ╞ ╟ 
# ╠ ╡ ╢ ╣ ╤ ╥ ╦ ╧ ╨ ╩ ╪ ╫ ╬ 

# sC.mainBoard.x = sC.board.genBoard(10,10)
# borderCluser = [["┏","━","━","━","━","━","━","━","━","┓"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┃"," "," "," "," "," "," "," "," ","┃"],["┗","━","━","━","━","━","━","━","━","┛"]]
# testCluster = [["h","e","l","l","o"],["w","o","r","l","d"]]

# gho.addCluster(testCluster,1,2)
# gho.addCluster(gho.cluster.straight.vertical,1,4)
# gho.addCluster(gho.cluster.straight.vertical,1,5)
# gho.addCluster(gho.cluster.straight.vertical,1,6)
# # gho.addCluster(borderCluser,0,0)
# sC.mainBoard.x = gho.charcterMap
# gho.printBoard(10,10)

gho.biuldMap(10,10)


# 0 0 0 1
# 1 0 1
# 0 1

# print(gho.wallMap[0][0].checkDeadEnd())
# junctDrirection = gho.wallMap[0][0].chooseJunction()
# print(junctDrirection)
# cordsNew = gho.wallMap[0][0].goDirection(junctDrirection)
# print(cordsNew)
# gho.mazeStackCell.addToPath(0,0)
# gho.wallMap[0][0].visited = True

# print("---------------------")

# while len(gho.mainStackPath) > 0:
#     currnetX = cordsNew[0]
#     currentY = cordsNew[1]
#     if gho.wallMap[currnetX][currentY].checkDeadEnd():
#         gho.mazeStackCell.backTrack()
#         print(gho.wallMap[currnetX][currentY].checkDeadEnd())
#     else:
#         junctDrirection = gho.wallMap[currnetX][currentY].chooseJunction()
#         print(junctDrirection)
#         cordsNew = gho.wallMap[currnetX][currentY].goDirection(junctDrirection)
#         print(cordsNew)
#         gho.mazeStackCell.addToPath(currnetX,currentY)
#         gho.wallMap[currnetX][currentY].visited = True
#     print(gho.mainStackPath)
#     print("---------------------")




gho.wallMap[0][0].makeMaze()
gho.inlineMap = sC.board.genBoard(30,30)
gho.mazeStackCell.removeWalls()
gho.mazeStackCell.generateMapInline()
sC.mainBoard.x = gho.inlineMap
gho.printBoard(30,30)
