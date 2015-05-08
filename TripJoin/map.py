#!/usr/bin/python

import sys
import string

for line in sys.stdin:

    values = line.strip().split(",")

    if values[0] in ('medallion'):  # skip first line 
        continue 
    
    # determine whether trip or fare by length of data 
    if len(values) == 11:   # fares file
        #0000 and 1111 there for debugging
        output = ','.join(values[:4] + [str(2222)] + values[4:]) 
        print output
    elif len(values) == 14:  # trips file
        output = ','.join(values[:3] + [values[5]] + [str(1111)] + values[3:5] + values[6:])
        print output
    else: # checked, never happens
        continue
