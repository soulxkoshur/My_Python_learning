import random


def main():
    x = get_level()
    s = 0
    for i in range(10):
        a = generate_integer(x)
        b = generate_integer(x)
        t = 3
        while t > 0:
            try:
                result = int(input(f"{a} + {b} = "))
                if result == a + b:
                    s += 1
                    break
                else:
                    print("EEE")
                    t -= 1
            except ValueError:
                continue
        if t == 0:
            print(f"{a} + {b} = {a+b}")
    print(s)





def get_level():
    while True:
        try:
            level = int(input("level: "))
            if 0 < level < 4:
                return level
            else:
                pass
        except ValueError:
            pass
        except KeyError:
            pass


def generate_integer(level):
    if level == 1:
         return random.randint(0,9)
    elif level == 2:
         return random.randint(10,99)
    elif level == 3:
         return random.randint(100,999)

if __name__ == "__main__":
    main()
