#!/usr/bin/python

import sys

current_month = None
total_revenue = 0.0
total_tip = 0.0

for line in sys.stdin:
    values = line.strip().split(',') 

    pickup = values[0]
    pickup_month = pickup.split('-')[1]

    tip = float(values[1]) 
    revenue = float(values[2]) 
   
    if pickup_month == current_month:
        total_revenue += revenue 
        total_tip += tip
    else:
        if current_month:
            # calculate tip percentage
            try:
                tipperc = total_tip/total_revenue*100.0
                tipperc = "%.2f" % round(tipperc,2)
            except ZeroDivisionError:
                tipperc = 0.0

            print ',\t'.join([current_month, str(total_tip), str(total_revenue), str(tipperc)])
 
        current_month = pickup_month 
        total_revenue = revenue
        total_tip = tip

try:
    tipperc = total_tip/total_revenue*100.0
    tipperc = "%.2f" % round(tipperc,2)
except ZeroDivisionError:
    tipperc = 0.0

print ',\t'.join([current_month, str(total_tip), str(total_revenue), str(tipperc)])
