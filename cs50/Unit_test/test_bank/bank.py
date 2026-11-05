def main():
    greeting = input("type a greeting: ")
    x = value(greeting)
    print(f"${x}")


def value(greeting):
    inp = greeting.casefold().strip()
    if "hello" in inp:
        return 0
    elif inp.endswith("h",0,1):
        return 20
    else: 
        return 100


if __name__ == "__main__":
    main()