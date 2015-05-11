import json
import numpy as np
import ogr


def centroid(vertices, area):

    xsum = 0
    ysum = 0
    xs = vertices[:, 0]
    ys = vertices[:, 1]

    norm = 1. / (6 * area)

    n = len(vertices)

    for i in range(n):
        xsum += (xs[i] + xs[(i + 1) % n]) * (xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i])
        ysum += (ys[i] + ys[(i + 1) % n]) * (xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i])

    cen = norm * np.array([xsum, ysum])

    return cen


# open census tract shapefile and get polygons
drv = ogr.GetDriverByName('ESRI Shapefile')

in_ds = drv.Open("../dat/nyct2010_15a/nyct2010.shp")

in_lyr = in_ds.GetLayer(0)

# # get set up for centroid output
# out_ds = drv.CreateDataSource("nycentroids.shp")
# out_lyr_poly = out_ds.CreateLayer("nycpoly", geom_type=ogr.wkbPolygon)
# out_lyr_cens = out_ds.CreateLayer()

# set up to make coordinate transformation from silly one to GPS
nyc_ref = in_lyr.GetSpatialRef() # ogr.osr.SpatialReference()
#nyc_ref.ImportFromEPSG(2263)
gps_ref = ogr.osr.SpatialReference()
gps_ref.ImportFromEPSG(4326)
ctran = ogr.osr.CoordinateTransformation(nyc_ref, gps_ref)

# initialise output array
outarr = np.zeros((in_lyr.GetFeatureCount(), 3))

# calculate centroid for each tract
for i in range(in_lyr.GetFeatureCount()):

    feat = in_lyr.GetFeature(i)
    geom = feat.geometry()

    area = geom.Area()

    vertdict = geom.ExportToJson()
    verts = json.loads(vertdict)
    vs = np.array(verts["coordinates"][0])

    c = centroid(vs, area)
    print c

    cpt = ogr.Geometry(ogr.wkbPoint)
    cpt.SetPoint_2D(0, c[0], c[1])
    cpt.Transform(ctran)

    [lon, lat, z] = ctran.TransformPoint(c[0], c[1], 0)
#    lon = cpt.GetX()
#    lat = cpt.GetY()
    print lon, lat

    outarr[i, 1] = lon
    outarr[i, 2] = lat

    # now get the tract's unique identifier
    id = float(feat.GetField("CTLabel"))

    outarr[i, 0] = id

np.savetxt("tract_centroids.dat", outarr)
