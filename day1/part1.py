#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re
x = 0
y = 0
facing = 0 # no instruction has been set

# get instructions from input
for line in sys.stdin:
    instructions = line.split(',')

for instruction in instructions:
    # remove space and new line
    instruction = re.sub(r'^\s',"",instruction)
    instruction = re.sub(r'\n',"",instruction)
    # print instruction

    # obtain direction and weight
    direction = re.sub(r'\d',"",instruction)
    weight = re.sub(r'^[LR]',"",instruction)

    # check if right
    right = re.search (r'R\d', instruction)

    # change direction
    #     1
    #  4  +  2
    #     3
    # if right
    if right:
        if (facing == 0):
            facing = 2
        elif (facing == 1):
            facing = 2
        elif (facing == 2):
            facing = 3
        elif (facing == 3):
            facing = 4
        elif (facing == 4):
            facing = 1
    # if left
    else:
        if (facing == 0):
            facing = 4
        elif (facing == 1):
            facing = 4
        elif (facing == 2):
            facing = 1
        elif (facing == 3):
            facing = 2
        elif (facing == 4):
            facing = 3

    # change x-y coordinates based on direction
    #     1
    #  4  +  2
    #     3
    if (facing == 1):
        y = y + int(weight)
    if (facing == 2):
        x = x + int(weight)
    if (facing == 3):
        y = y - int(weight)
    if (facing == 4):
        x = x - int(weight)

# print y distance from start
print abs(x)+abs(y)
