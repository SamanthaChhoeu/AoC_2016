#!/usr/bin/python
# test...python part1.py < input.txt

import sys,re

code = [] # store the code pattern
prev = 5 # start at 5

for line in sys.stdin:
#      1
#   2  3  4
# 5  6  7  8  9
#   10 11 12
#      13
# A - 10, B - 11, C - 12, D - 13
    # starting key
    key = prev

    for letter in line:
        letter = re.sub(r'\s',"",letter) # remove spaces
        up = re.search (r'U', letter)
        down = re.search (r'D', letter)
        left = re.search (r'L', letter)
        right = re.search (r'R', letter)

        if up:
            if key == 5 or key == 2 or key == 1 or key == 4 or key == 9:
                key = key
            else:
                if key == 3 or key == 13:
                    key = key + 2
                else:
                    key = key - 4
        elif down:
            if key == 5 or key == 10 or key == 13 or key == 12 or key == 9:
                key = key
            else:
                if key == 1 or key == 11:
                    key = key + 2
                else:
                    key = key + 4
        elif left:
            if key == 1 or key == 2 or key == 5  or key == 10  or key == 13:
                key = key
            else:
                key = key -1
        elif right:
            if key == 1 or key == 4 or key == 9  or key == 12  or key == 13:
                key = key
            else:
                key = key + 1
    prev = key # remember previous key
    code.append(key)

print code
