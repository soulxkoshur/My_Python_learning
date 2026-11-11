import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    pattern = r""
    match = re.match(pattern, ip)
    if match:
        return True
    else:
        return False

...


if __name__ == "__main__":
    main()