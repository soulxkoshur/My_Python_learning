import sys
import csv


def main():
    try:
        if len(sys.argv)<3:
            sys.exit("Too few command-line arguments")
        elif len(sys.argv)>3:
            sys.exit("Too many command-line arguments")
        else:
            read_csv(sys.argv[1], sys.argv[2])
    except FileNotFoundError:
        sys.exit(f"Could not read ... {sys.argv[1]}")
def read_csv(before, after):
    with open(before, "r") as before, open(after, "w", newline="") as after:
        reader = csv.DictReader(before)
        writer = csv.DictWriter(after, fieldnames=['first', 'last', 'house'])
        writer.writeheader()
        for row in reader:
            last, first = row['name'].strip().split(', ')
            writer.writerow ({"first": first, "last": last, "house": row['house']})



if __name__== "__main__":
    main()


