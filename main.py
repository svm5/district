import argparse

from geocoder import get_coordinates, geocode, get_district


parser = argparse.ArgumentParser()
parser.add_argument("address", nargs="*")
address = " ".join(parser.parse_args().address)

coords = get_coordinates(address)
# print(coords)
res = geocode(str(coords[0]) + "," + str(coords[1]), kind="district")
print(get_district(res))