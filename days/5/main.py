# Advent of code Year 2025 Day 5 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)

lines = input.splitlines()

db = set()

def isInDb(num):
    for start, end in db:
        if num >= start and num <= end:
            return True
    return False

def isInsideInterval(currentPair, candidatePair):
    [candStart, candEnd] = candidatePair
    [currStart, currEnd] = currentPair
    if candStart >= currStart and candStart <= currEnd and candEnd >= currStart and candEnd <= currEnd:
        return True

def updateDb(newStart, newEnd):
    candidatePair = (newStart, newEnd)
    write = True
    for pair in db.copy():
        [start, end] = pair
        if isInsideInterval(pair, candidatePair):
            print(f'\t{candidatePair} inside of {pair}')
            write = False
        # Start is in interval, end is not
        elif newStart >= start and newStart <= end and newEnd > end and pair in db:
            print(f'\t{candidatePair} overlaps {pair} -- recursing on {start}-{newEnd}')
            db.remove(pair)
            write = False
            updateDb(start, newEnd)
        # Start is not in interval, end is
        elif newStart < start and newEnd >= start and newEnd <= end and pair in db:
            print(f'\t{candidatePair} overlaps {pair} -- recursing on {newStart}-{end}')
            db.remove(pair)
            write = False
            updateDb(newStart, end)
        # They contain the interval
        elif newStart < start and newEnd > end and pair in db:
            print(f'\t{candidatePair} contains {pair}')
            db.remove(pair)

    if write:
        print(f'\t\tinserting {candidatePair}')
        db.add(candidatePair)

fresh = 0
for line in lines:
    if '-' in line:
        [startStr, endStr] = line.split('-')
        # candidatePair = (int(startStr), int(endStr))
        print(f'adding {line}')
        updateDb(int(startStr), int(endStr))
    # elif line != '':
    #     if isInDb(int(line)):
    #         fresh += 1

# print(fresh)

total = 0 
for pair in db:
    [start, end] = pair
    newSum = int(end) - int(start) + 1
    print(f'Adding {newSum} for {pair}')
    total += newSum
    
print()
print(total)
