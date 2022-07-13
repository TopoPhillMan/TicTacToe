import squareControl as sC
import gameControl as gC
import ticFunctions as tic
import connectFunctions as con
import golfFunctions as golf
import math

class ball():
    x = int
    y = int
    sprite = ""
    weight = int # Kilos

mainBall = ball()

def calcAirTime(yInitial, velocityInitial, gravity, angle):
    # yInital = velocityY*time + (0.5*gravity)*time**2
    # time = (-1*(velocityY) +- sqrt(velocityY**2 -4*(0.5*gravity)*yInitial)) / 0.5*gravity

    velocityY = velocityInitial*math.sin(math.radians(angle))
    squareRootValue = velocityY**2 -4*(0.5*gravity)*yInitial
    if yInitial >= 0:
        time = (-1*velocityY - math.sqrt(squareRootValue)) / 0.5*gravity
    elif yInitial < 0:
        time = (-1*(velocityY) + math.sqrt(velocityY**2 -4*(0.5*gravity)*yInitial)) / 0.5*gravity
    
    return time

