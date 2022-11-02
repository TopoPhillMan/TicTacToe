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
gho.biuldMap(10,10)
# gho.addCluster(testCluster,1,2)
# gho.addCluster(gho.cluster.straight.vertical,1,4)
# gho.addCluster(gho.cluster.straight.vertical,1,5)
# gho.addCluster(gho.cluster.straight.vertical,1,6)
# # gho.addCluster(borderCluser,0,0)
# sC.mainBoard.x = gho.charcterMap
# gho.printBoard(10,10)

gho.wallMap[0][0].visited = True
gho.wallMap[1][0].visited = True


gho.wallMap[0][0].makeMaze()
print('a')

