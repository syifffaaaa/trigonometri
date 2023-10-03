from math import radians, cos, sin, asin, sqrt

lokasi1 = input("masukan lokasi pertama :")
lokasi2 = input("masukan lokasi kedua :")
lon1 = float(input("masukan longitude1 :"))
lat1 = float(input("masukan latitude1 :"))
lon2 = float(input("masukan longitude2 :"))
lat2 = float(input("masukan latitude2 :"))


def haversine(lat1, lon1, lat2, lon2):
    KM = 6372.8  # this is in KM.  For Earth radius in miles use 3959.87433 miles

    dLat = radians(lat2 - lat1)
    dLon = radians(lon2 - lon1)
    lat1 = radians(lat1)
    lat2 = radians(lat2)

    a = sin(dLat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dLon / 2) ** 2
    c = 2 * asin(sqrt(a))

    return KM * c



hasil = haversine(lat1, lon1, lat2, lon2)

print(
    f"""
Jadi jarak antara {lokasi1} dan {lokasi2} adalah {hasil} kilometer
"""
)
