from turtle import clearscreen
import gameControl as gC
import squareControl as sC
import ticFunctions as tic
import connectFunctions as con

def play():
    print("""
What Game do you want to play
1. TicTackToe
2. Connect 4""")
    gameChoice = int(input("> "))
    if gameChoice == 1:
        print("""
What game style would you like to use?
1. Clasic: 3x3 Board, Win Length 3
2. Large: 5x5 board, Win Length 5
3. Weird: 5x5 board, Win length 3
4. Costom
        """)
        gameStyleChoice = int(input("> "))
        if gameStyleChoice == 1:
            gC.clearScreen()
            tic.ticTackToeMainLoop(3,3,3)
        if gameStyleChoice == 2:
            gC.clearScreen()
            tic.ticTackToeMainLoop(5,5,5)
        if gameStyleChoice == 3:
            gC.clearScreen()
            tic.ticTackToeMainLoop(5,5,3)
        if gameStyleChoice == 4:
            tic.ticTackToeMainLoop(int(input("How Wide is the Board\n > ")),int(input("How Tall is the Board\n > ")),int(input("How Long to Win\n > ")))
    elif gameChoice == 2:
        gC.clearScreen()
        print("""
What game style would you like to use?
1. Clasic: 6x6 Board, Win Length 4
2. Large: 10x10 board, Win Length 5
3. Weird: 4x4 board, Win length 3
4. Costom
        """)
        gameStyleChoice = int(input("> "))
        if gameStyleChoice == 1:
            gC.clearScreen()
            con.connectFourMainLoop(6,6,4)
        if gameStyleChoice == 2:
            gC.clearScreen()
            con.connectFourMainLoop(10,10,5)
        if gameStyleChoice == 3:
            gC.clearScreen()
            con.connectFourMainLoop(4,4,3)
        if gameStyleChoice == 4:
            con.connectFourMainLoop(int(input("How Wide is the Board\n > ")),int(input("How Tall is the Board\n > ")),int(input("How Long to Win\n > ")))
    else:
        print("Invalid Input")

play()
