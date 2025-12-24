# Advent of code Year 2025 Day 10 solution
# Author = Drew Blocki
# Date = December 2025

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

import scipy

from utils import get_input
from itertools import combinations_with_replacement, permutations
from scipy.optimize import linprog

input = get_input(__file__)
lines = input.splitlines()

maxPresses = []

def isValid(buttonPressPerm):
    for buttonIndex, presses in enumerate(buttonPressPerm):
        if presses > maxPresses[buttonIndex]:
            return False
    return True

# You want to:
#   - Minimize: sum(x) (total button presses)
#   - Subject to: Ax = b (each counter reaches its target)
#   - And: x >= 0 (can't press negative times)

#   This is exactly what scipy.optimize.linprog does:

#   from scipy.optimize import linprog

#   # c = coefficients for objective function (minimize c·x)
#   # A_eq, b_eq = equality constraints (Ax = b)
#   c = [1] * num_buttons  # minimize sum of all presses
#   result = linprog(c, A_eq=A, b_eq=targets, bounds=(0, None))
#   # result.x gives you the solution, result.fun gives the minimum total

# Thank you Claude
def generateSumPermutations(n, target_sum):
    result = []
    # Generate all combinations that sum to target
    for combo in combinations_with_replacement(range(target_sum + 1), n):
        if sum(combo) == target_sum:
            # Get all unique permutations of this combination
            perms = permutations(combo)
            permList = list(set(perms))
            for nextPerm in permList:
                if isValid(nextPerm):
                    result.append(nextPerm)
    return [list(perm) for perm in result]
# End Claude

# Part 1 checking
def comboMatchesLightSolution(combo, buttonConfigList, solution):
    on = set()
    for index, char in enumerate(solution):
        if char == '#':
            on.add(index)
    lightToggles = [0] * len(solution)
    for i in combo:
        buttonConfig = buttonConfigList[i]
        for lightIndex in buttonConfig:
            lightToggles[lightIndex] += 1
    for lightIndex, toggleCount in enumerate(lightToggles):
        if toggleCount % 2 == 1 and lightIndex not in on:
            return False
        elif toggleCount % 2 == 0 and lightIndex in on:
            return False
    return True

# Part 2 checking
def comboMatchesJoltageSolution(combo, buttonConfigList, solution):
    lightCounts = [0] * len(solution)
    quit = False
    for buttonIndex, pressCount in enumerate(combo):
        button = buttonConfigList[buttonIndex]
        for lightIndex in button:
            lightCounts[lightIndex] += pressCount
            if lightCounts[lightIndex] > solution[lightIndex]:
                quit = True
                break
        if quit:
            break
    if quit:
        return False
    for lightIndex, joltageCount in enumerate(lightCounts):
        if joltageCount != solution[lightIndex]:
            return False
    return True 

lineNum = 1
total = 0
for line in lines:
    parts = line.split()
    
    # Part 1
    solution1Str = parts[0]
    solution1 = solution1Str[1:-1]
    
    # Part 2
    solution2StrFull = parts[-1]
    solution2Str = solution2StrFull[1:-1]
    solution2 = [int(joltageStr) for joltageStr in solution2Str.split(',')]
    
    buttons = parts[1:-1]
    numButtons = len(buttons)
    buttonConfigList = []
    for lightConfig in buttons:
        lightConfigStrList = lightConfig[1:-1].split(',')
        buttonConfigList.append([int(light)for light in lightConfigStrList])

    print(f'{lineNum}/{len(lines)}\tSolving {solution2}')
    indexList = [i for i in range(numButtons)]
    
    # Part 1
    # n = 1
    # Part 2
    n = max(solution2)
    
    # maxPresses = [n for _ in range(numButtons)]
    # for joltageIndex, joltage in enumerate(solution2):
    #     for buttonIndex, buttonConfig in enumerate(buttonConfigList):
    #         if joltageIndex in buttonConfig:
    #             maxPresses[buttonIndex] = min(maxPresses[buttonIndex], joltage)
    
    # print(f'\t\tmax presses: {maxPresses}')
    
    # while True:
    #     print(f'\tAttempting combos of size {n}')
    #     # combinations = list(combinations_with_replacement(indexList, n))
    #     combinations = generateSumPermutations(numButtons, n)
    #     print(f'\t\tgenerated {len(combinations)} perms')
        
    #     success = False
    #     for combo in combinations:
    #         # if comboMatchesLightSolution(combo, buttonConfigList, solution1):
    #         #     total += n
    #         #     success = True
    #         #     print(f'\tSolved with {n} presses')
    #         #     break
    #         if comboMatchesJoltageSolution(combo, buttonConfigList, solution2):
    #             total += n
    #             success = True
    #             print(f'\tSolved with {n} presses')
    #             break
    #     if success:
    #         break
    #     n += 1
    
    c = [1] * numButtons
    A = []
    for solIndex, _ in enumerate(solution2):
        nextArr = []
        for button in buttonConfigList:
            if solIndex in button:
                nextArr.append(1)
            else:
                nextArr.append(0)
        A.append(nextArr)
    targets = solution2
    # print(f'\tsolving:')
    # print(f'\t\t{A}')
    # print(f'\t\t{targets}')
    result = linprog(c, A_eq=A, b_eq=targets, bounds=(0, None), integrality=c)
    # print(f'\tresult:')
    # print(f'\t\t{result.x}')
    print(f'\t{result.fun}')
    if not result.success:
        assert False

    total += result.fun
    lineNum += 1
        
print()
print(total)
print(scipy.__version__)