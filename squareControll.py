

class boardSquare:
    value = "-"

class rowX:
    y = []

class board:
    x = []

def makeBoard(xHight,yHight):
    mainBoard = board()
    for x in range(xHight):
        board.x.append(rowX)
        for a in range(yHight):
            board.x[0].y.append(boardSquare)

makeBoard(3,3)
