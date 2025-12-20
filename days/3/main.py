# Advent of code Year 2025 Day 3 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)

cache = {}
def getCache(line, n):
    if line in cache and n in cache[line]:
        return cache[line][n]
    return None
    
def setCache(line, n, val):
    if line in cache:
        cache[line][n] = val
    else:
        cache[line] = {}
        cache[line][n] = val

def getBankMaxOf2(line):
    if getCache(line, 2):
        return getCache(line, 2)
    bankMax = 0
    for indexLeft in range(len(line)):
        leftVal = int(line[indexLeft])
        if leftVal * 10 + 9 < bankMax:
            continue
        for indexRight in range(indexLeft + 1, len(line)):
            rightVal = int(line[indexRight])
            potential = 10 * leftVal + rightVal
            if potential > bankMax:
                bankMax = potential
    # print(f'found max of {bankMax} for {line} (length 2)')
    setCache(line, 2, bankMax)
    return bankMax

def getBankMaxOfN(line, n):
    if getCache(line, n):
        return getCache(line, n)
    if n == 2:
        return getBankMaxOf2(line)
    if n > len(line):
        # print(f'returning {int('0' * n)} for {line} (length {n})')
        return int('0' * n)
    if n == len(line):
        # print(f'found max of {int(line)} for {line} (length {n})')
        return int(line)
    bankMax = 0
    for indexLeft in range(len(line) - n):
        leftVal = int(line[indexLeft])
        if int(f'{leftVal}{'9' * (n - 1)}') < bankMax:
            continue
        candidateWithLeft = leftVal * pow(10, n - 1) + getBankMaxOfN(line[indexLeft + 1:], n - 1)
        candidateWithout = getBankMaxOfN(line[indexLeft + 1:], n)
        bestCandidate = max(candidateWithLeft, candidateWithout)
        if bestCandidate > bankMax:
            bankMax = bestCandidate
    # print(f'found max of {bankMax} for {line} (length {n})')
    setCache(line, n, bankMax)
    return bankMax

total = 0
n = 12

lines = input.splitlines()
for line in lines:
    bankMax = getBankMaxOfN(line, n)
    print(f'found max of {bankMax} for {line}')
    total += bankMax

# line = '234278'
# total += getBankMaxOfN(line, 5)

print()
print(total)