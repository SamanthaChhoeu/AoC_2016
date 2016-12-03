#!/usr/bin/perl -w

# store code
code = []

# read line
    # new key
    key = 0
    # read each character
        # up
            # if 1,2,3 then stop and store number
            # otherwise subtract 3 from key
        # down
            # if 7,8,9 then stop and store number
            # otherwise add 3 to key
        # left
            # if 1,4,7 then stop and store number
            # otherwise subtract 3 from key
        # right
            # if 3,6,9 then stop and store number
            # otherwise add 1 to key
