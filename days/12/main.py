# Advent of code Year 2025 Day 12 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
sections = input.split('\n\n')

multipler = 7

totalValid = 0
for line in sections[6].splitlines():
    parts = line.split(' ')

    [wStr, hStr] = parts[0][:-1].split('x')
    w = int(wStr)
    h = int(hStr)
    size = w * h
    
    partSum = 0
    for part in parts[1:]:
        partCount = int(part)
        partSum += partCount
    
    if partSum * multipler < size:
        print(f'VALID: \t\t{line}')
        totalValid += 1
    else:
        print(f'INVALID: \t{line}')

print()
print(totalValid)
