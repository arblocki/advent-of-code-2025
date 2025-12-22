# Advent of code Year 2025 Day 7 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
lines = input.splitlines()

numLines = len(lines)
numCols = len(lines[0])

# beam = set()
splitters = set()

beamStart = (0, 0)

cache = {}
def getCachedVal(line, col):
    if line in cache and col in cache[line]:
        return cache[line][col]
    return None

def setCachedVal(line, col, val):
    if line in cache:
        cache[line][col] = val
    else:
        cache[line] = {}
        cache[line][col] = val

for lineIndex, line in enumerate(lines):
    for charIndex, i in enumerate(range(len(line))):
        char = line[i]
        if char == 'S':
            beamStart = (lineIndex, charIndex)
        elif char == '^':
            splitters.add((lineIndex, charIndex))

def simulateBeam(start):
    [lineI, charI] = start
    cachedVal = getCachedVal(lineI, charI)
    if cachedVal:
        return cachedVal
    print(f'simulating from {start}')
    nextLine = lineI + 1
    if nextLine == numLines:
        setCachedVal(lineI, charI, 1)
        return 1
    candidate = (nextLine, charI)
    if candidate in splitters:
        total = 0
        if charI != 0:
            total += simulateBeam((nextLine, charI - 1))
        if charI + 1 < numCols:
            total += simulateBeam((nextLine, charI + 1))
        setCachedVal(lineI, charI, total)
        return total
    else:
        total = simulateBeam(candidate)
        setCachedVal(lineI, charI, total)
        return total

total = simulateBeam(beamStart)

print(total)
