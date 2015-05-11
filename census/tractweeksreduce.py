#!/usr/bin/python

import sys
import numpy as np

current_tract = None
full_count = 0
current_week = None
cred_count = 0
tip_tot = 0

for line in sys.stdin:
    values = line.strip().split(',') 

    weekno = int(values[0])
    tract = int(values[1])
    iscrd = values[2]
    tip = float(values[3]) 

    if weekno == current_week:
        if tract == current_tract:
            full_count += 1

            if iscrd == "CRD":
                cred_count += 1
                tip_tot += tip

        else:
            if current_tract:
                cred_count += 1  # in case it's zero
                print "{0}\t{1}\t{2}\t{3}".format(str(weekno), str(current_tract), str(full_count), str(tip_tot / cred_count))
            current_tract = tract
            full_count = 1
            if iscrd == "CRD":
                cred_count = 1
                tip_tot = tip
            else:
                cred_count = 0
                tip_tot = 0
    else:
        if weekno:
            cred_count += 1
            print "{0}\t{1}\t{2}\t{3}".format(str(current_week), str(current_tract), str(full_count), str(tip_tot / cred_count))
        current_week = weekno
        current_tract = tract
        full_count = 1
        if iscrd == "CRD":
            cred_count = 1
            tip_tot = tip
        else:
            cred_count = 0
            tip_tot = 0

cred_count += 1
print "{0}\t{1}\t{2}\t{3}".format(str(current_week), str(current_tract), str(full_count), str(tip_tot / cred_count))

