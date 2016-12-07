#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re

# sum of sector ids
sum = 0

for line in sys.stdin:
    chars = {}
    line = re.sub(r'\n$',"",line) # remove new line
    # for each character that isnt a -

    print line
print sum
