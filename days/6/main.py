# Advent of code Year 2025 Day 6 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
lines = input.splitlines()

numLists = []
for i in range(len(lines[0].split())):
    numLists.append([])

# --------------------------------------------------------------------
# Part 1 processing
# for line in input.splitlines()[:-1]:
#     nums = line.split()
#     for index, num in enumerate(nums):
#         numLists[index].append(num)

# --------------------------------------------------------------------

# Part 2 processing
# Calculate splits
lastOpIndex = 0
splits = []
for index, char in enumerate(lines[-1]):
    if char != ' ' and index != 0:
        splits.append(index - lastOpIndex - 1)
        lastOpIndex = index
splits.append(len(lines[0]) - lastOpIndex)

# for each split: process each line and put all nums into list
indexProcessed = 0
for splitIndex, split in enumerate(splits):
    rangeStart = indexProcessed + split - 1
    rangeEnd = indexProcessed - 1
    for i in range(rangeStart, rangeEnd, -1):
        # Build string of each line char at i, then convert to int and add to list
        numStr = ''
        for line in lines[:-1]:
            numStr += line[i]
        numLists[splitIndex].append(int(numStr))
    indexProcessed += split + 1
    print(f'\tbuilt list for split {splitIndex}: {numLists[splitIndex]}')

# --------------------------------------------------------------------

total = 0
for index, operator in enumerate(lines[-1].split()):
    nextList = numLists[index]
    if operator == '*':
        curr = 1
        for num in nextList:
            curr *= int(num)
        total += curr
    else:
        curr = 0
        for num in nextList:
            curr += int(num)
        total += curr
    
print(total)
