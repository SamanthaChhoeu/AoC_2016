#!/usr/bin/python
# test... python solution.py input
# only one arg at a time

# I KNOW THIS IS BAD STYLE BUT I DID IT ON THE
# PLANE WITH NO INTERNET LOL SORRY

# BUG: HAVENT ACCOUNTED FOR IF ( open bracket is just there
# BUG: OR HAVENT ACCOUNTED FOR (3x1)(( < two brackets
# BUG: HAVENT ACCOUNTED FOR NUMBERS MORE THAN ONE DIGIT LOL OOPS
import sys, re

count   = 0 # keeps track of length
bracket = 0 # flag for reading inside bracket
string = []  # array of characters in input

# infrmation of repetition
length = 0 # length of string to repeat
times  = 0 # number of times to repeat

# read input from stdin
# append each character to array
for line in sys.stdin:
    line = re.sub(r'\n$',"",line) # remove new line
    line = re.sub(r'\r',"",line)  # remove \r
    line = re.sub(r'\s',"",line)  # remove space
    for char in line:
        string.append(char)

# initialise i - used to identify character in string
i = 0
while i in range(0,len(string)):
    # get char to look at
    char = string[i]
    print char
    # when to stop checking pattern to repeat
    stop = 0
    # if the length of repeated pattern is exceeded
    # change flag to 0
    if i > stop and bracket == 1:
        bracket = 0
    # if open bracket
    if char == "(":
        # ignore bracket if flag is set
        if bracket == 1:
            count +=1
        # otherwise figure out length when bracket is decompressed
        elif bracket == 0:
            bracket = 1 # set flag
            length = int(string[i+1])
            stop = length + i # set length where the pattern stops
            times = int(string[i+3])
            # increment 4 to move past close bracket
            i += 4
            # j represents characters after brackets to check if they are repeated
            for j in range(0, int(length)):
                # if j is longer than string, stop there and mult
                if j > len(string):
                    length = j
                # if j is shorter than string, decrement to remove repeats
                # from the else below
                else:
                    count -= 1
            # calculation: count + length*times
            count = count+length*times
    # if its just a normal character increment
    else:
        count += 1
    # increment i
    i+=1
print count
