
from math import dist


distances = {
    "Voyager 1": "163",
    "Voyager 2": "136",
    "Pioneer 10": "80 AU",
    "New Horizons": "58",
    "Pioneer 11": "44 AU",
}


def main():
    spacecraft = input("Enter a spacecraft name: ")
    try:
        au = float(distances[spacecraft])
    except KeyError:
        print(f"'{spacecraft}' is not in the distances dictionary.")
        return
    except ValueError:
        print(f"cant convert distance '{distances[spacecraft]}' to float.")
        return
    m = convert(au)
    print(f"The distance to {spacecraft} is {m} meters.")


def convert(au):
    return au * 149597870700


main()
