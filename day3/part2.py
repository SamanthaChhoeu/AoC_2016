#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re
first = []
second = []
third = []

# get lines from input
for line in sys.stdin:
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'^\s+',"",line) # remove space at beginning
    line = re.sub(r'\s+$',"",line)
    line = re.sub(r'\s+'," ",line) # change whitespace to one space
    sides = line.split(' ')
    #sides.sort(key = int)
    first.append(sides[0])
    second.append(sides[1])
    third.append(sides[2])

def count(sides):
    count = 0 # count of triangles
    tri = [0,0,0]
    for i in range (0,len(sides)-2):
        if (i%3 == 0):
            x=i+1
            y=i+2
            tri[0] = sides[i]
            tri[1] = sides[x]
            tri[2] = sides[y]
            tri.sort(key = int)
            if (int(tri[0])+int(tri[1]) > int(tri[2])):
                count += 1
    return count

triangles = count(first)
triangles = triangles + count(second)
triangles = triangles + count(third)

print triangles
