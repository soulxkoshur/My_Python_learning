import sys
def main():
    coordinates_t = (42.3, -71.1)
    # above is how we make a tuple.
    coordinates_l = [42.3, -71.1]
    print(f"longitude: {coordinates_t[0]}, latitude: {coordinates_t[1]}")
    longitude, latitude = coordinates_t
    print(f"longitude: {longitude}, latitude: {latitude}")
    print(f"size of tuple: {sys.getsizeof(coordinates_t)}, size of list: {sys.getsizeof(coordinates_l)}")

main()
