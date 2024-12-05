import math
def areacircle(diam):
    radius = diam / 2
    radsquare = radius * radius
    area = math.pi * radsquare
    return area
def perimcircle(diam):
    radius = diam / 2
    circum = 2 * math.pi * radius
    return circum

def rectanglearea(w,h):
    area = w * h
    return area
def rectangleperim(w,h):
    perim = (w*2) + (h*2)
    return perim