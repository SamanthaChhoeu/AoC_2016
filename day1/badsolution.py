# GIVES CORRECT ANSWER BUT IMPLEMENTATION IS WEIRD
# so i misinterpreted the question,
# and thought right meant 45 degrees (ie NE)
# and left meant -45 degrees (ie NW)

import sys,re
x = 0
y = 0
facing = 0 # no instruction has been set

# 4 \  / 1
#    \/
#    /\
# 3 /  \ 2

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
    # if right
    if right:
        if (facing == 0):
            facing = 1
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
    if (facing == 1):
        x = x + int(weight)
        y = y + int(weight)
    if (facing == 2):
        x = x + int(weight)
        y = y - int(weight)
    if (facing == 3):
        x = x - int(weight)
        y = y - int(weight)
    if (facing == 4):
        x = x - int(weight)
        y = y + int(weight)

# print y distance from start
print abs(y)
#print abs(x)+abs(y)
