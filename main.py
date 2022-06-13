from numpy import square
import gameControl as gC
import squareControl as sC
import testing as test

print("""
 WELCOME TO TICTACKTOE
 ---------------------
   by Calvin Corbett

 Rules: 
 Players will take turns placing a game peice (X or O)
 into the playable area by selecting the X and Y cordinate of
 the square they wish to put their peice in.

 In order to win one player will have to place 3 peices into
 a uninterupted line, either horizontaly, verticaly, or diagonly.

 If no winner is chosen at the end of the game, then a restart
 will occor and players will try and wonder what went wrong. 

 HAVE FUN!
 
""")


while gC.gameContinues:
  gC.mainLoop(3,3,3)
  print("Game Restarting due to Full Board")