#!/usr/bin/python

import sys
import numpy as np
from scipy.spatial import cKDTree


tracts = np.loadtxt("../dat/tract_centroids.dat")
tractcens = tracts[:, 1:]

tractree = cKDTree(tractcens)


for line in sys.stdin:
    values = line.strip().split(",")    # split values of TripFareTip
    
    long1 = float(values[4])
    lat1 = float(values[5])
    long2 = float(values[6])
    lat2 = float(values[7])

    d, tract1 = tractree.query(np.array([long1, lat1]))
    d, tract2 = tractree.query(np.array([long2, lat2]))

    print ','.join([str(tract2), str(tract1)] + values)  #output
