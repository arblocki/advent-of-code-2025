# Advent of code Year 2025 Day 11 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

from utils import get_input

input = get_input(__file__)
lines = input.splitlines()

server = {}
outs = {}
for line in lines:
    parts = line.split()
    head = parts[0][:-1]
    tails = parts[1:]
    server[head] = tails
    
head = 'svr'
dac = 'dac'
fft = 'fft'

def convertListToStr(list):
    res = ''
    for str in list:
        res += str
    return res

def findNumOuts(head, need):
    print(f'\trunning {head} with need: {need}')
    needStr = convertListToStr(need)
    if (head, needStr) in outs:
        return outs[(head, needStr)]
    tails = server[head]
    if tails[0] == 'out':
        res = 0
        if len(need) == 0:
            res = 1
        print(f'\t\trecording ({head}, {needStr}) as {res}')
        outs[(head, needStr)] = res
        return res
    total = 0
    newNeed = need.copy()
    if head == dac and dac in need:
        newNeed.remove(dac)
    elif head == fft and fft in need:
        newNeed.remove(fft)
    for tail in tails:
        total += findNumOuts(tail, newNeed)
    outs[(head, needStr)] = total
    return total

print(findNumOuts(head, [dac, fft]))