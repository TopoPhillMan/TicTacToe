from functools import cache
from random import random, randrange
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
mapBoard = sC.board()

def changeAlt(startX,startY,altGain):
    for x in range(abs(altGain)):
        if altGain > 0: 
            golf.mapBoard.x[startX+x][startY+x] = "╱"
        if altGain == 0:
            golf.mapBoard.x[startX+x][startY] = "_"
        if altGain < 0:
            golf.mapBoard.x[startX+x][startY-(x+1)] = f"╲"

def addStraight(startX,startY,length):
    for x in range(length):
        golf.mapBoard.x[startX+x][startY] = "_"

def genMap():
    startAlt = int

    startAlt = round(0.25*golf.mapBoard.yRows)
    operatingCache = int
    operatingPosX = 3
    operatingPosY = startAlt
    operatingContinue = True


    golf.mapBoard.x[0][startAlt] = "_"
    golf.mapBoard.x[1][startAlt] = "▄"
    golf.mapBoard.x[2][startAlt] = "_"

    while operatingContinue:
        if operatingPosX >= 0.50*golf.mapBoard.xRows:
            operatingContinue = False
            continue

        operatingCache = round(((golf.mapBoard.xRows - 3)*0.4)*random())
        golf.addStraight(operatingPosX, operatingPosY, operatingCache)
        operatingPosX += operatingCache

        operatingCache = random()
        if operatingCache <= 0.25:
            operatingCache = -2
        elif operatingCache > 0.25 and operatingCache <= 0.5:
            operatingCache = -1
        elif operatingCache > 0.5 and operatingCache <= 0.75:
            operatingCache = 1
        elif operatingCache > 0.75 and operatingCache <= 1:
            operatingCache = 2

        if operatingPosY + operatingCache < 1:
            operatingCache = abs(operatingCache)

        golf.changeAlt(operatingPosX,operatingPosY,operatingCache)
        operatingPosX += (abs(operatingCache))
        operatingPosY += operatingCache

    operatingCache = golf.mapBoard.xRows - operatingPosX
    golf.addStraight(operatingPosX, operatingPosY, operatingCache)

    operatingContinue = (golf.mapBoard.xRows-1) - round(0.8*(operatingCache*random()))
    golf.mapBoard.x[operatingContinue][operatingPosY] = "ˌ"
    golf.mapBoard.x[operatingContinue][operatingPosY-1] = "˅"

def resetMap():
    xRows = golf.mapBoard.xRows
    yRows = golf.mapBoard.yRows
    for x in range(xRows):
        for y in range(yRows):
            golf.mapBoard.x[x][y] = " "

def calcAirTime(yChange, velocityInitial, gravity, angle):
    # y = yInital + velocityY*time + (0.5*gravity)*time**2
    # time = (-1*(velocityY) +- sqrt(velocityY**2 -4*(0.5*gravity)*yInitial)) / 0.5*gravity

    velocityY = velocityInitial*math.sin(math.radians(angle))
    squareRootValue = velocityY**2 -4*(0.5*gravity)*yChange
    if yChange >= 0:
        time = (-1*velocityY - math.sqrt(squareRootValue)) / 0.5*gravity
    elif yChange < 0:
        time = (-1*(velocityY) + math.sqrt(velocityY**2 -4*(0.5*gravity)*yChange)) / 0.5*gravity
    
    return time


