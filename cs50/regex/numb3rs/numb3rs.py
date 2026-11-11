import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Making a pattern for a range is hard!
    #for dns i can simply split!
    pattern = r"^\d(\d\d)?\.\d(\d\d)?\.\d(\d\d)?\.\d(\d\d)?$"
    matches = re.search(pattern, ip)
    if matches:
        return inrangeip(ip)
    else:
        return False


    

def inrangeip(number):

    a, b, c, d = number.split('.')
    return 0<int(a) <= 255 and int(b) <= 255 and int(c) <= 255 and int(d) <= 255


if __name__ == "__main__":
    main()