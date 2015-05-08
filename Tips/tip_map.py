#!/usr/bin/python

import sys
import string

for line in sys.stdin:
    values = line.strip().split(",")    # split values of TripFareJoin 
    
    pick_up = values[3]     # pick up time

    n_pass = values[7]      # number of passengers
    trip_time = values[8]   # trip time in seconds 
    trip_dist = values[9]   # trip distance 

    pickup_long = values[10]     # pick up longitude
    pickup_lat = values[11]     # pick up latitude
    
    dropoff_long = values[12]   # drop off longitude
    dropoff_lat = values[13]    # drop off latitude 

    payment_type = values[14] 

    fare = values[15]
    surcharge = values[16]
    tip = values[18]
    toll = values[19]
    total = values[20]
    
    print ','.join([ pick_up, 
        n_pass, trip_time, trip_dist, 
        pickup_long, pickup_lat, dropoff_long, dropoff_lat, 
        payment_type, fare, tip, toll, surcharge, total
        ])  #output
