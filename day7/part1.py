#!/usr/bin/python
# test... python solution.py < input.txt

# I KNOW THIS IS BAD STYLE BUT I DID IT ON THE
# PLANE WITH NO INTERNET LOL SORRY

import sys,re

count = 0 # count of IPs that support TLS

# search string for abba
# return 1 if match, 0 if no match
def abba(string):
    char = []
    contains = 0
    for character in string:
        char.append(character)
    # find ABBA
    for i in range(0, len(char)-3):
        #print char[i]
        #print char[i+3]
        if char[i] == char[i+3] and char[i+1] == char[i+2] and char[i]!=char[i+1]:
            contains = 1
    return contains

for line in sys.stdin:
    flag = 0
    line = re.sub(r'\s\n',"",line)
    # get contents of brackets
    brackets =  re.findall('\[.*?\]',line)
    for bracket in brackets:
        content = re.sub(r'\[',"",bracket)
        content = re.sub(r'\]',"",content)
        if abba(bracket) == 1:
            flag = 1
    # no ABBA
    if abba(line)==0:
        count += 0;
    # ABBA in square brackets
    elif flag == 1:
        count += 0;
    elif abba(line) == 1:
        count = count + 1;
    # SUPPORT TLS - ABBA outside brackets
print count
