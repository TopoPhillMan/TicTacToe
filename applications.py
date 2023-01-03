import controllers.gameControl as gC
import controllers.squareControl as sC
import assets.ticFunctions as tic
import assets.connectFunctions as con
import assets.ghostFunctions as gho
import sys 
import os

def main():
    if len(sys.argv) == 1:
        print("""
    -=Welcome to Tic Tac Toe=- 

    Please select a usage for the program.

    -TicTacToe-
    Tic Tac Toe is a two person 1 vs 1 board game. It involves
    two players taking alternating turns, while placing peices on
    the board, with the objective being to secure the desired 
    number of concurent peices in either, horizontal, vertical, or 
    diagonoal axis.  

        python3 ticTackToe.py tic [xDimension][yDimension][winLength]

    -Connect 4-
    Connect 4 is a two player, 1 vs 1 board game. It involves 
    players taling turns palcing peices intp collums of a board
    where they stack verticaly. The game is won, when a player
    the designated number of peices in a row, in either horizontal, 
    vertical, or diagonoal axis.  

        python3 ticTackToe.py con [xDimension][yDimension][winLength]

    -Maze-
    Generate a maze of a specified size, with text characters.

        python3 ticTackToe.py maze [xDimension] [yDimension] 

        """)
        return(0)
    if sys.argv[1] == "tic":
        ticApp()
    elif sys.argv[1] == "con":
        conApp()
    elif sys.argv[1] == "maze":
        mazeApp()
    else:
        print("Error - Impropper Terms Used")

def ticApp():
    if len(sys.argv) == 2:
        print("""
    -=Welcome to Tic Tack Toe=-

    Tic Tac Toe is a two person 1 vs 1 board game. It involves
    two players taking alternating turns, while placing peices on
    the board, with the objective being to secure the desired 
    number of concurent peices in either, horizontal, vertical, or 
    diagonoal axis.  

    =Rules=
    - Each person takes their turn one after another
    - Durring a turn a person will place their given peice on the board
    whether that be an (X) or an (O)
        - You cannot replace peices that have already placed 
        - You can only place once per turn
    - A game is completed by obtaining the desited number of peices in a row
        - This can be done in the Horizontal, Vertical, or Diagonal
        - The peices must me contiguous 
    - In the even that there is no way a player can win, the game restarts

    =Using this Program=
    In order to use this program, you must input a set up board dimensions,
    as well as the length deisted for a win. This is done by first typing, 
    `python3 tictacktoe tic`, followed by the x dimension, y dimension, and 
    win length, `python3 tictacktoe <xLength> <yLength> <winLength>`. An 
    exsample, for the regular game would be...
        - python3 ticTackToe.py tic 3 3 3
    
        """)
        delayInput = input("<Press Enter to Continue>")
        gC.clearScreen()

        x = int(input("X Dimension > "))
        y = int(input("Y Dimension > "))
        w = int(input("Win Length > "))
        tic.ticTackToeMainLoop(x,y,w)
        exit()

    elif len(sys.argv) < 5:
        print("Missing Values! - Type `python3 ticTackToe.py tic` for help")
        exit()
    elif len(sys.argv) > 5:
        print("Too Many Values! - Type `python3 ticTackToe.py tic` for help")
        exit()
    else:
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        w = int(sys.argv[5])
        tic.ticTackToeMainLoop(x,y,w)

def conApp():
    if len(sys.argv) == 1:
        print("""
    -=Welcome to Connect 4=-
    
    Connect 4 is a two player, 1 vs 1 board game. It involves 
    players taling turns palcing peices intp collums of a board
    where they stack verticaly. The game is won, when a player
    the designated number of peices in a row, in either horizontal, 
    vertical, or diagonoal axis.  
        
    =Rules=
    - Each person takes their turn one after another
    - Durring a turn a person will place their given peice in a collum of choice
    whether that be an (X) or an (O)
        - You cannot replace peices that have already placed 
        - You can only place once per turn
    - A game is completed by obtaining the desited number of peices in a row
        - This can be done in the Horizontal, Vertical, or Diagonal
        - The peices must me contiguous 
    - In the even that there is no way a player can win, the game restarts

    =Using this Program=
    In order to use this program, you must input a set up board dimensions,
    as well as the length deisted for a win. This is done by first typing, 
    `python3 tictacktoe con`, followed by the x dimension, y dimension, and 
    win length, `python3 tictacktoe.py <xLength> <yLength> <winLength>`. An 
    exsample, for the regular game would be...
        - python3 ticTackToe.py con 7 7 4
        """)
        delayInput = input("<Press Enter to Continue>")
        gC.clearScreen()

        x = int(input("X Dimension > "))
        y = int(input("Y Dimension > "))
        w = int(input("Win Length > "))
        con.connectFourMainLoop(x,y,w)

    elif len(sys.argv) < 5:
        print("Missing Values! - Type `python3 tictacktoe.py con` for help")
        exit()
    elif len(sys.argv) > 5:
        print("Too Many Values! - Type `python3 tictacktoe.py con` for help")
        exit()
    else:
        x = int(sys.argv[3])
        y = int(sys.argv[4])
        w = int(sys.argv[5])
        con.connectFourMainLoop(x,y,w)
    
def mazeApp():
    if len(sys.argv) == 2:
        print("""
    -= Welcome to Maze=-

    This function will generate a maze of a specified size, with text 
    characters.

    -Usage- 

    python3 ticTackToe.py maze [xDimension] [yDimension] 

        """)
        delayInput = input("<Press Enter to Continue>")
        gC.clearScreen()

        x = int(input("X Dimension > "))
        y = int(input("Y Dimension > "))
        gho.generateFull(x,y) 
    elif len(sys.argv) == 3: 
        print("Too Few Values!")
    elif len(sys.argv) > 4:
        print("Too many values")
    else: 
        x = int(sys.argv[3])
        gho.generateFull(int(sys.argv[3]),int(sys.argv[4]))






    