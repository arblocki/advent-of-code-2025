# Advent of code Year 2025 Day 4 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
lines = input.splitlines()

cleared = set()
paper = set()
rowCount = len(lines)
colCount = len(lines[0])

def isPaper(row, col):
    if (row, col) in paper:
        return 1
    return 0

def countNearbyPaper(row, col):
    count = 0
    count += isPaper(row - 1, col - 1)
    count += isPaper(row - 1, col)
    count += isPaper(row - 1, col + 1)
    
    count += isPaper(row, col - 1)
    count += isPaper(row, col + 1)
    
    count += isPaper(row + 1, col - 1)
    count += isPaper(row + 1, col)
    count += isPaper(row + 1, col + 1)
    return count
    
def clearPaper():
    totalCleared = 0
    for rowIndex, colIndex in paper:
        if countNearbyPaper(rowIndex, colIndex) < 4:
            cleared.add((rowIndex, colIndex))
            totalCleared += 1
    paper.difference_update(cleared)
    return totalCleared

for lineIndex, line in enumerate(lines):
        for charIndex, char in enumerate(line):
            if char == '@':
                paper.add((lineIndex, charIndex))

total = 0
numCleared = 1
while numCleared > 0:
    numCleared = clearPaper()
    total += numCleared
    print(f'clearing {numCleared}')

print()
print(len(cleared))

