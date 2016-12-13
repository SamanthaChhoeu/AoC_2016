#!/usr/bin/python
# test... python solution.py < input.txt
# answer in test input is 3

import sys,re

count = 0 # count of IPs

# aba[bab] # ie pattern outside, reverse pattern inside

# find pattern
# return 1 if match, 0 if no match
# retun list of patterns that match aba
def aba(string):
    char = []
    patterns = [] # keep track of aba patterns
    contains = 0
    for character in string:
        char.append(character)
    # find ABBA
    for i in range(0, len(char)-3):
        #print char[i]
        #print char[i+3]
        if char[i].isalpha() and char[i+1].isalpha() and char[i+2].isalpha():
            if char[i] == char[i+2] and char[i+1] != char[i]:
                contains = 1
                pattern = char[i]+char[i+1]+char[i+2]
                patterns.append(pattern)
    print patterns
    return contains, patterns

for line in sys.stdin:
    flag = 0
    line = re.sub(r'\s\n',"",line)
    # get contents of brackets
    brackets =  re.findall('\[.*?\]',line)
    for bracket in brackets:
        content = re.sub(r'\[',"",bracket)
        content = re.sub(r'\]',"",content)
        if aba(bracket) == 1:
            flag = 1
    # stuff outside brackets
    outside = re.sub(r'\[.*\]',"",line)
    print line
    match, patterns = aba(line)
    # no ABA in whole string
    if match == 0:
        count += 0;
    elif match == 1:
        if ()
        count = count + 1
    print count
print count
