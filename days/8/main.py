# Advent of code Year 2025 Day 8 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
lines = input.splitlines()

def calcDistance(one, two):
    return pow(one[0] - two[0], 2) + pow(one[1] - two[1], 2) + pow(one[2] - two[2], 2)

circuitMap = {}
points = []
circuitSizes = []
connectedPoints = set()

# merge points in circuit j to circuit i
def mergeCircuits(circuitI, circuitJ):
    for point in points:
        if circuitMap[point] == circuitJ:
            circuitMap[point] = circuitI
            circuitSizes[circuitI] += 1
            circuitSizes[circuitJ] -= 1
            
def countNonZeroCircuits():
    total = 0
    for i in range(len(circuitSizes)):
        if circuitSizes[i] > 0:
            total += 1
    return total

def getCircuitIndex():
    for i in range(len(circuitSizes)):
        if circuitSizes[i] > 0:
            return i

for line in lines:
    coordStrs = line.split(',')
    [xStr, yStr, zStr] = coordStrs
    coord = (int(xStr), int(yStr), int(zStr))
    circuitMap[coord] = -1
    points.append(coord)

nextCircuit = 0
n = 1000

finalI = (0, 0, 0)
finalJ = (0, 0, 0)

distMap = {}
distList = []
for i in range(len(points) - 1):
    distMap[i] = {}
    for j in range(i + 1, len(points)):
        dist = calcDistance(points[i], points[j])
        distMap[i][j] = dist
        distList.append((dist, (i, j)))
        
def firstItemComparator(e):
  return e[0]
distList.sort(key=firstItemComparator)

distIndex = 0
while True:
    minDistance = sys.maxsize
    minI = -1
    minJ = -1
    # for i in range(len(points) - 1):
    #     for j in range(i + 1, len(points)):
    #         dist = distMap[i][j]
    #         if dist < minDistance and (i, j) not in connectedPoints:
    #             minDistance = dist
    #             minI = i
    #             minJ = j
    distItem = distList[distIndex]
    minDistance = distItem[0]
    minI = distItem[1][0]
    minJ = distItem[1][1]
    distIndex += 1
    
    iCoords = points[minI]
    jCoords = points[minJ]
    iCircuit = circuitMap[iCoords]
    jCircuit = circuitMap[jCoords]
    connectedPoints.add((minI, minJ))
    # print(f'found min distance of {minDistance} between {iCoords} and {jCoords}')
    
    # Neither are in a circuit
    if iCircuit == -1 and jCircuit == -1:
        # print(f'\tadding them to circuit {nextCircuit}')
        circuitMap[iCoords] = nextCircuit
        circuitMap[jCoords] = nextCircuit
        assert nextCircuit == len(circuitSizes)
        circuitSizes.append(2)
        nextCircuit += 1
    # One is in a circuit, the other isn't
    elif iCircuit != -1 and jCircuit == -1:
        # print(f'\tadding {jCoords} to circuit {iCircuit}')
        circuitMap[jCoords] = iCircuit
        circuitSizes[iCircuit] += 1
    elif iCircuit == -1 and jCircuit != -1:
        # print(f'\tadding {iCoords} to circuit {jCircuit}')
        circuitMap[iCoords] = jCircuit
        circuitSizes[jCircuit] += 1
    # They're already in the same circuit -- do nothing
    # They're in different circuits
    elif iCircuit != jCircuit:
        # print(f'\merging circuit {jCircuit} into circuit {iCircuit}')
        mergeCircuits(iCircuit, jCircuit)
    
    if countNonZeroCircuits() == 1 and circuitSizes[getCircuitIndex()] == len(points):
        finalI = iCoords
        finalJ = jCoords
        break

# print()
# print(f'circuits: {circuitSizes}')

# circuitSizes.sort(reverse=True)

# print()
# print(f'circuits: {circuitSizes}')
# product = circuitSizes[0] * circuitSizes[1] * circuitSizes[2]

# print()
# print(product)

print()  
print(finalI[0] * finalJ[0])
