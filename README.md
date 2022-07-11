# TicTackToe
TicTackToe is a program that allows users to play the games of Tic Tack Toe and Connect 4 via a python command line in their system. As well as allowing for these games to be played in their classic state, or on modified boards with modified win conditions TicTackToe uses a python environment within a users terminal so that the program is usable by anyone, no matter their operating system or computational requirements.

## Installation
At its core TicTackToe is a python script (```main.py``` specifically) that can be run in your command line of choice, via an installation of python 3. There are more in depth instructions on how to get everything set up for this program, but that is the most basic form of how to get TicTackToe running and if you are more experienced with python and its function, that should be all you need, if not, then continue reading.

### Installing Python
If you already have python installed feel free to skip this step,

Installing python is a relatively simple procedure. You will first want to go to the python website (https://www.python.org/downloads/), and locate the latest version of python 3 available for your type of system, and then download it to your machine. Once that completes navigate to the python installer and open it. Then, after making sure the box next to ```Add Python 3 to PATH``` is clicked, go ahead and take the ```Install Now``` option, and continue through setup.

In order to check that everything was successful, go to your command line of choice and simply type ```python```, if your system doesn't throw an error, then you should be good to go. If it does throw an error, make sure that Python was added to PATH, and was installed correctly. 

### Running TicTackToe
Once you have python installed, running TicTackToe should be a relatively straightforward process. Download the latest version of the source code from https://github.com/TopoPhillMan/TicTackToe/releases, and unpack the .zip to a location anywhere on your system. You will next want to navigate to this location via a command line, and then type the command ```python main.py``` and you should be away and playing TicTackToe.

## Playing the Game
### Tic Tack Toe
Tic Tack Toe is a game in which two players attempt to connect a set amount of their pieces in a row (Vertical, Horizontal, or Diagonal) before their opponent does, with each player being able to place anywhere on the board. 

In this program Tic Tack Toe is played using a coordinate grid, where users select the X (Horizontal) position of their next piece, and then the Y (Vertical) position of their next piece before the opponent goes on with their next turn. This allows a single square to be precisely selected within the board, and while it takes some getting used to, this allows the easiest use within a terminal. 

### Connect 4
Connect 4 is a game in which two players attempt to connect a set amount of pieces in a row (Vertical, Horizontal, or Diagonal) before their opponent dose, with players filling the columns of the board (Bottom to Top) as its main differentiation from Tic Tack Toe. 

In this program Connect 4 is played with users selecting the column that they with to place into, and nothing more. Giving an easier play experience, and faster to learn terminal variation on the original game.

