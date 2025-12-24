# Advent of code Year 2025 Day 9 solution
# Author = Drew Blocki
# Date = December 2025

# FUCK

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input
from math import comb
from operator import itemgetter

input = get_input(__file__)
lines = input.splitlines()

tiles = []
eligible = set()
ineligible = set()

xLen = 0
yLen = 0
for line in lines:
    [xStr, yStr] = line.split(',')
    x = int(xStr)
    y = int(yStr)
    xLen = max(x + 1, xLen)
    yLen = max(y + 1, yLen)

tileMap = [['.' for _ in range(yLen)] for _ in range(xLen)]

def connectTiles(tile1, tile2):
    [x1, y1] = tile1
    [x2, y2] = tile2
    if x1 == x2:
        minY = min(y1, y2)
        maxY = max(y1, y2)
        for y in range(minY + 1, maxY):
            tileMap[x1][y] = 'O'
            eligible.add((x1, y))
    else:
        minX = min(x1, x2)
        maxX = max(x1, x2)
        for x in range(minX + 1, maxX):
            tileMap[x][y1] = 'O'
            eligible.add((x, y1))

mostRecent = None
for line in lines:
    [xStr, yStr] = line.split(',')
    x = int(xStr)
    y = int(yStr)
    xLen = max(x + 1, xLen)
    yLen = max(y + 1, yLen)
    point = (x, y)
    tiles.append(point)
    eligible.add(point)
    tileMap[x][y] = 'O'
    if mostRecent:
        connectTiles(mostRecent, point)
    mostRecent = point

[xStr, yStr] = lines[0].split(',')
x = int(xStr)
y = int(yStr)
connectTiles(mostRecent, (x, y))

print('Marking ineligible')
for y in range(yLen):
    for x in range(xLen):
        if (x, y) in eligible:
            break
        tileMap[x][y] = 'X'
    for x in range(xLen - 1, -1, -1):
        if (x, y) in eligible:
            break
        tileMap[x][y] = 'X'
    print(f'{y + 1}\t/\t{yLen}')

def printMap():
    for y in range(yLen):
        lineStr = ''
        for x in range(xLen):
            if (x, y) in eligible:
                lineStr += 'X'
            elif (x, y) in ineligible:
                lineStr += 'O'
            else:
                lineStr += '.'
        print(lineStr)
    print()
    
# printMap()

def calcSize(tile1, tile2):
    xDiff = abs(tile1[0] - tile2[0]) + 1
    yDiff = abs(tile1[1] - tile2[1]) + 1
    return xDiff * yDiff

# Space is eligible if you can go in every direction and find an eligible space before hitting the border
def isSpaceEligible(x, y):
    if tileMap[x][y] != 'X':
        return True
    else:
        return False
    
    # if (x, y) in eligible:
    #     return True
    # # Check up
    # for nextY in range(y, -1, -1):
    #     if (x, nextY) in eligible:
    #         break
    #     if nextY == 0:
    #         return False
    # # Check down
    # for nextY in range(y, yLen):
    #     if (x, nextY) in eligible:
    #         break
    #     if nextY == yLen - 1:
    #         return False
    # # Check left
    # for nextX in range(x, -1, -1):
    #     if (nextX, y) in eligible:
    #         break
    #     if nextX == 0:
    #         return False
    # # Check right
    # for nextX in range(x, xLen):
    #     if (nextX, y) in eligible:
    #         break
    #     if nextX == xLen - 1:
    #         return False
    # eligible.add((x, y))
    # return True

# Check if every square in the rectangle is eligible
def isValidRectangle(tile1, tile2):
    [x1, y1] = tile1
    [x2, y2] = tile2
    
    minX = min(x1, x2)
    maxX = max(x1, x2)
    minY = min(y1, y2)
    maxY = max(y1, y2)
    
    for x in range(minX, maxX + 1):
        if not isSpaceEligible(x, minY):
            return False
    for x in range(minX, maxX + 1):
        if not isSpaceEligible(x, maxY):
            return False
        
    for y in range(minY, maxY + 1):
        if not isSpaceEligible(minX, y):
            return False
    for y in range(minY, maxY + 1):
        if not isSpaceEligible(maxX, y):
            return False

    return True

maxSize = 0

n = 1
total = comb(len(tiles), 2)

sizeArr = []
for i in range(len(tiles) - 1):
    for j in range(i + 1, len(tiles)):
        tileI = tiles[i]
        tileJ = tiles[j]
        size = calcSize(tileI, tileJ)
        sizeArr.append((size, tileI, tileJ))
        print(f'{n} \t/\t{total}')
        n += 1

print()
print('sorting...')
sortedSizes = sorted(sizeArr, key=itemgetter(0), reverse=True)
print()

n = 1
for i in range(total):
    element = sortedSizes[i]
    size = element[0]
    isValid = isValidRectangle(element[1], element[2])
    if isValid:
        print(size)
        break

    print(f'{n} \t/\t{total}')
    n += 1

# print()
# print(maxSize)
