import sys

def main():
    while True:
        try:
            if len(sys.argv) < 2:
                print("Too few command-line arguments")
                sys.exit(1)

            elif not sys.argv[1].endswith(".py"):
                sys.exit("Not a Python file")
            elif len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            else:
                number = numberoflines(sys.argv[1])
                print(number)
                break
        except FileNotFoundError:
            sys.exit("File not found")  

def numberoflines(x):
    number = 0
    with open( x, "r") as f:
        content = f.readlines()
        for line in content:
            if line.lstrip().startswith("#") or line.strip() == "":
                continue
            else:
                number += 1
    return number

main()