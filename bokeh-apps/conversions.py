import math
         
def geo_to_web_lon(x_lon):
    num = x_lon * 0.017453292519943295
    x = 6378137.0 * num
    return x

def geo_to_web_lat(y_lat):
    a = y_lat * 0.017453292519943295
    y_mercator = 3189068.5 * math.log((1.0 + math.sin(a)) / (1.0 - math.sin(a)))
    return y_mercator