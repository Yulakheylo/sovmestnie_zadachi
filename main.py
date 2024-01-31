import sys
from geocoder import get_coordinates, get_ll_span
from mapapi import show_map

toponym_to_find = " ".join(sys.argv[1:])
if toponym_to_find:
    lat, lon = get_coordinates(toponym_to_find)
    ll_spn = f"ll={lat},{lon}&spn=0.005,0.005"
    show_map(ll_spn, "map")

    ll, spn = get_ll_span(toponym_to_find)
    ll_spn = f"ll={ll}&spn={spn}"
    show_map(ll_spn, "map")

    point_param = f"pt={ll}"
    show_map(ll_spn, "map", add_params=point_param)
else:
    print('No data')