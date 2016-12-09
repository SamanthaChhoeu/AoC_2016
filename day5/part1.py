#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re
for line in sys.stdin:
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'\s',"",line) # remove space
    hash = 00000%int(line)
    print hash
    for letter in line:
        print letter
