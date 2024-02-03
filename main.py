import sys
from business import find_business
from geocoder import get_coordinates
from distance import lonlat_distance
from mapapi import show_map

toponym_to_find = " ".join(sys.argv[1:])

lat, lon = get_coordinates(toponym_to_find)
address_ll = f"{lat},{lon}"
span = "0.005,0.005"

organization = find_business(address_ll, span, "аптека")
point = organization["geometry"]["coordinates"]
org_lat, org_lon = float(point[0]), float(point[1])

points_param = f"pt={org_lat},{org_lon},pm2dgl~{address_ll},pm2rdl"
show_map(f"ll={address_ll}&spn={span}", "map", add_params=points_param)

show_map(map_type="map", add_params=points_param)

try:
    name = organization["properties"]["CompanyMetaData"]["name"]
    address = organization["properties"]["CompanyMetaData"]["address"]
    time = organization["properties"]["CompanyMetaData"]["Hours"]["text"]
    distance = round(lonlat_distance((lon, lat), (org_lon, org_lat)))
    snippet = f"Название:\t{name}\nАдрес:\t{address}\nВремя работы:\t{time}\nРасстояние:\t{distance}м."
    print(snippet)
except KeyError:
    print("Ошибка. Не указаны данные.")