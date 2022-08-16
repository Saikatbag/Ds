import json
from math import pi, sin, cos, sqrt, asin


def find_dist(latlng_1, latlng_2):
    lat1, lon1 = latlng_1[0]*pi/180, latlng_1[1]*pi/180
    lat2, lon2 = latlng_2[0]*pi/180, latlng_2[1]*pi/180
    d = 2*6371*asin(sqrt(sin((lat2-lat1)/2)**2 + cos(lat1)*cos(lat2)*sin((lon2-lon1)/2)**2))
    return round(d,2)

file = "../text.json"

limit = 0

with open(file, 'r') as f:
    contries = json.load(f)
first_20 = {}
for contry in contries:
    if contry['population'] >= limit:
        first_20[contry['alpha3Code']] = contry['latlng']
        if len(first_20) == 20:
            break

total_dist = 0
keys = list(first_20.keys())
print( first_20[keys[1]])
for i in range(len(keys)-1):
    
    total_dist += find_dist(first_20[keys[i]], first_20[keys[i+1]])
total_dist = round(total_dist, 2)


print(total_dist)