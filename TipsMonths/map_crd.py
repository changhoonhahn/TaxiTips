#!/usr/bin/python

import sys
import string

for line in sys.stdin:
    values = line.strip().split(",")    # split values of TripFareJoin 
    
    pick_up = values[0]     # pick up time
    payment_type = (values[8]).strip() 

    tip = values[11]
    total = values[13]

    if float(total) == 0.0: 
        continue

    if payment_type == 'CRD': 
        print ','.join([ pick_up, tip, total])  #output
    else: 
        continue 
