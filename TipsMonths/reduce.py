#!/usr/bin/python

import sys

current_day = None

for line in sys.stdin:
    values = line.strip().split(',') 

    pickup = values[0] 
    tip = float(values[1]) 
    total = float(values[2]) 
    
    try: 
        fare = float(values[9])
    except ValueError: 
        continue  

    tip = float(values[10])
    toll = float(values[11])
    surcharge = float(values[12])
    total = float(values[13]) 
    
    if (total == 0.0) or (fare == 0.0): 
        # useless
        continue 

    try: 
        tipperc = tip/total*100.0
        tipperc = "%.2f" % round(tipperc,2)
    except ZeroDivisionError: 
        tipperc = 0.0

    print ',\t'.join([pickup, 
        n_pass, trip_time, trip_dist,
        pickup_long, pickup_lat, dropoff_long, dropoff_lat, 
        payment_type, str(fare), str(tip), str(toll), str(surcharge), str(total), str(tipperc)
        ]) 
