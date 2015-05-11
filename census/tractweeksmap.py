#!/usr/bin/python

import sys
import datetime
import numpy as np
from scipy.spatial import cKDTree


tracts = np.loadtxt("../dat/tract_centroids.dat")
tractcens = tracts[:, 1:]

tractree = cKDTree(tractcens)


for line in sys.stdin:
    values = line.strip().split(",")    # split values of TripFareTip

    time = values[0]
    ymd = time.split()[0].split("-")

    weekno = datetime.date(int(ymd[0]), int(ymd[1]), int(ymd[2])).isocalendar()[1]
    
    droplong = float(values[6])
    droplat = float(values[7])

    d, tract = tractree.query(np.array([droplong, droplat]))

    print ','.join([str(weekno), str(tract)] + [values[8]] + [values[-1]])  #output
