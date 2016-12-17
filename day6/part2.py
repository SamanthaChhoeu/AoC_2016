#!/usr/bin/python
# test... python solution.py < input.txt


# I KNOW THIS IS BAD STYLE BUT I DID IT ON THE
# PLANE WITH NO INTERNET LOL SORRY

import sys,re
flag=0 # using this because im on the plane and
       # i dont know if you can check if empty
positions = {}
word = []
for line in sys.stdin:
    line = re.sub(r'\n',"",line)
    line = re.sub(r'\r',"",line)
    size =  len(line)
    i = 0

    characters = []

    for char in line:
        characters.append(char)
    if flag == 0:
        for char in characters:
            positions[i]=char
            flag = 1
            i+=1
    else:
        for char in characters:
            stuff = positions[i]
            positions[i]=stuff+char
            i+=1
for i in positions:
    frequency = {}
    for char in positions[i]:
        if char in frequency:
            frequency[char]+=1
        else:
            frequency[char]=1
    # PART 2 - change to min not max
    min = 0
    for char in frequency:
        if min == 0:
            min = frequency[char]
            character = char
            print word
        else:
            if min>frequency[char]:
                min = frequency[char]
                character = char
                print word
    word.append(character)
print word
