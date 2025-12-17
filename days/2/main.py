# Advent of code Year 2025 Day 2 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)

total = 0

ranges = input.split(',')
for nextRange in ranges:
    [beginStr, endStr] = nextRange.split('-')
    begin = int(beginStr)
    end = int(endStr)
    # print(f'iterating over range {begin}-{end}')
    for nextId in range(begin, end + 1):
        idString = str(nextId)
        idLen = len(idString)
        for dividend in range(2, idLen + 1):
            if idLen % dividend != 0:
                continue
            segmentLen = idLen // dividend
            candidate = idString[:segmentLen]
            pointer = segmentLen
            weird = True
            while pointer < idLen:
                if idString[pointer:pointer + segmentLen] != candidate:
                    weird = False
                    break
                pointer += segmentLen
            
            # print(f'checking {idString} (len: {idLen}) -- {idString[:median]} {idString[median:]}')
            if weird:
                print(f'found special number: {nextId}')
                total += nextId
                break

print()
print(f'total: {total}')
