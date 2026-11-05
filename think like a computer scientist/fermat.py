from math import *

a, b, c = input( "type any three numbers, for formula a^n + b^n = c^n \n").split()
n = input ("type any power \n")
x = (int(a) ** int(n)) + (int(b) ** int(n))
y = int(c) ** int(n)    

def fermat():
    if int(n) > 2 and int(x) == int(y):
        print ("holy smokes, fermat was wrong")
    else:
        print("fermat was right, no such integers exist")
fermat()
print ("the value of a^n + b^n is: " + str(int(x)))
print ("the value of c^n is: " + str(int(y)))