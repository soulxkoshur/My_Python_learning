def main():
    while True:
        fraction = input("Enter fraction: ")
        try:
            result = convert(fraction)
            print(gauge(result))
            break
        except (ValueError, ZeroDivisionError):
            continue


def convert(fraction):
    
    x, y = fraction.split("/")
    x = int(x)
    y = int(y)

    
    if y == 0:
        raise ZeroDivisionError

    
    if x > y or x < 0 or y < 0:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()