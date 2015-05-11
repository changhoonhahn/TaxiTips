import json
import numpy as np
import ogr


def centroid(vertices):

    xsum = 0
    ysum = 0
    xs = vertices[:, 0]
    ys = vertices[:, 1]

    area = 0

    n = len(vertices)

    for i in range(n):
        area += xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i]

    area = 0.5 * area
    norm = 1. / (6 * area)

    for i in range(n):
        xsum += (xs[i] + xs[(i + 1) % n]) * (xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i])
        ysum += (ys[i] + ys[(i + 1) % n]) * (xs[i] * ys[(i + 1) % n] - xs[(i + 1) % n] * ys[i])

    cen = norm * np.array([xsum, ysum])

    return cen


# open census tract shapefile and get polygons
drv = ogr.GetDriverByName('ESRI Shapefile')

in_ds = drv.Open("../dat/nyct2010_15a/nyct2010.shp")

in_lyr = in_ds.GetLayer(0)

# get set up for centroid output
out_ds = drv.CreateDataSource("/Users/kilian/dev/TaxiTips/census/nycentroids.shp")
out_lyr = out_ds.CreateLayer("centroids", geom_type=ogr.wkbPoint)
id_field = ogr.FieldDefn("id", ogr.OFTReal)
out_lyr.CreateField(id_field)
out_feats = out_lyr.GetLayerDefn()

# calculate centroid for each tract
for i in range(in_lyr.GetFeatureCount()):

    feat = in_lyr.GetFeature(i)
    geom = feat.geometry()

    vertdict = geom.ExportToJson()
    verts = json.loads(vertdict)
    vs = np.array(verts["coordinates"][0])

    while len(vs.shape) > 2:
        vs = vs[0]
    print vs

    c = centroid(vs)
    print c

    # create a new feature to add to the output layer
    newfeat = ogr.Feature(out_feats)

    cpt = ogr.Geometry(ogr.wkbPoint)
    cpt.SetPoint_2D(0, c[0], c[1])

    newfeat.SetGeometry(cpt)

    # now get the tract's unique identifier
    id = float(feat.GetField("CTLabel"))

    newfeat.SetField("id", id)

    out_lyr.CreateFeature(newfeat)


