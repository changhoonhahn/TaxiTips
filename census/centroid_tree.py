import numpy as np
from scipy.spatial import cKDTree


tracts = np.loadtxt("../dat/tract_centroids.dat")
tractcens = tracts[:, 1:]

tractree = cKDTree(tractcens)

def find_tract(pt):
    d, i = tractree.query(pt)
    return i


