# Advent of code Year 2025 Day 1 solution
# Author = Drew Blocki
# Date = December 2025

with open((__file__.rstrip("main.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

current = 50
totalZero = 0

lines = input.splitlines()
for line in lines:
    direction = line[0]
    delta = int(line[1:])
    
    # Normalize delta between 0 and 99
    while delta >= 100:
        totalZero += 1
        delta -= 100
    
    if direction == 'L':
        current -= delta
        if current < 0:
            # Count the time we passed 0 if we didn't start at 0
            if (current + delta != 0):
                print(f'\tCrossed 0 moving left {delta}')
                totalZero += 1
            current += 100
    else:
        current += delta
        if current >= 100:
            # Only count another if we passed 0, not if we landed on it (same as 100)
            if current > 100:
                print(f'\tCrossed 0 moving right {delta}')
                totalZero += 1
            current -= 100
                
    
    if current == 0:
        totalZero += 1
    
    print(f'{line}\t{current}\t{totalZero}')

print()
print(totalZero)
