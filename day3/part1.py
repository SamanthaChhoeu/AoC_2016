#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re
triangles = 0 # count of triangles

# get lines from input
for line in sys.stdin:
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'^\s+',"",line) # remove space at beginning
    line = re.sub(r'\s*$',"",line) # remove space at end
    line = re.sub(r'\s+'," ",line) # change whitespace to one space
    sides = line.split(' ')
    sides.sort(key = int)
    #print sides
    sum = int(sides[0])+int(sides[1])
    #print sum
    if (sum > int(sides[2])):
        triangles = triangles + 1
print triangles
