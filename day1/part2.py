#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re
x = 0
y = 0
facing = 0 # no instruction has been set
visited = {} # keep track of visited coordinates

# get instructions from input
for line in sys.stdin:
    instructions = line.split(',')

for instruction in instructions:
    # remove space and new line
    instruction = re.sub(r'^\s',"",instruction)
    instruction = re.sub(r'\n',"",instruction)

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
    for i in range(0, int(weight)):
        if (facing == 1):
            y = y + 1
        if (facing == 2):
            x = x + 1
        if (facing == 3):
            y = y - 1
        if (facing == 4):
            x = x - 1

        # check if coord has been visited
        coord = x,y
        #print coord
        if coord in visited:
            print abs(x)+abs(y)
            sys.exit()
        else:
            visited[coord] = 1
