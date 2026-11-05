from pyfiglet import Figlet
import sys
from random import choice
figlet = Figlet()
list = figlet.getFonts()

try:
    if len(sys.argv) == 1:
           text = input("Input: ")
           figlet.setFont(font=choice(list))
           print(figlet.renderText(text))
    elif sys.argv[1] not in list and sys.argv[1] != '-f':
        raise ValueError

    else:
        text = input("Input: ")

        if sys.argv[2] in list:
            figlet.setFont(font=sys.argv[2])
            print(figlet.renderText(text))
        else:
            print("Invalid usage")
except ValueError:
    sys.exit("Invalid usage")
except IndexError:
    sys.exit("Invalid usage")
