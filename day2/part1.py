#!/usr/bin/python
# test...python part1.py < input.txt

import sys,re

code = [] # store the code pattern
prev = 5 # start at 5

for line in sys.stdin:
    # starting key
    key = prev

    for letter in line:
        letter = re.sub(r'\s',"",letter) # remove spaces
        up = re.search (r'U', letter)
        down = re.search (r'D', letter)
        left = re.search (r'L', letter)
        right = re.search (r'R', letter)

        if up:
            if key == 1 or key == 2 or key == 3:
                key = key
            else:
                key = key - 3
        elif down:
            if key == 7 or key == 8 or key == 9:
                key = key
            else:
                key = key + 3
        elif left:
            if key == 1 or key == 4 or key == 7:
                key = key
            else:
                key = key -1
        elif right:
            if key == 3 or key == 6 or key == 9:
                key = key
            else:
                key = key + 1
    prev = key # remember previous key
    code.append(key)

print code
