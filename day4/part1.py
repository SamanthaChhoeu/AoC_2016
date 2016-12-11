#!/usr/bin/python
# test... python solution.py < input.txt
import sys,re


# I KNOW THIS IS BAD STYLE BUT I DID IT ON THE
# PLANE WITH NO INTERNET LOL SORRY

# sum of sector ids
sum = 0

# find the find most common
# takes in dict
# return most common char
def common(dict):
    equal = [] # for characters that are equally frequent

    freq = 0
    char = 0
    for i in dict:
        # greater than highest
        if int(dict[i])>freq:
            freq = dict[i]
            char = i
            del equal[:]
            equal.append(char)
        # equal to highest
        elif int(dict[i]) == freq:
            equal.append(i)

    equal.sort()
    char = equal[0]
    del equal[:]
    dict[char] = -1
    return char
    # once we find the most common, set dict value to 0

for line in sys.stdin:
    # i = 0 to keep track of how many
    length = 0
    count = {}
    chars = {}
    check = [] # calculated checksum
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'\r',"",line)
    # get checksum
    checksum = re.sub(r"^.*\[","", line)
    checksum = re.sub(r"\]","", checksum)
    # get name
    name = re.sub(r"\[.*\]","", line)
    name = re.sub(r"\d","",name)
    # get sectorID
    sectorID = re.sub(r"\D","",line)
    #print "name is "+name
    #print "sector ID is "+sectorID
    #print "checksum is "+checksum
    # for each character that isnt a -

    for char in name:
        letter = re.match(r'[A-Za-z]', char)
        if letter:
            if char in count:
                count[char]+=1
            else:
                count[char]=1
    for i in range(0,5):
        # keep calling common
        char = common(count)
        check.append(char)
    #word = ''.join(check)
    checksumlist = []
    for i in checksum:
        checksumlist.append(i)
    if check == checksumlist:
        sum += int(sectorID)
print sum
