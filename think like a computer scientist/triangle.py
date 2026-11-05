import math

a, b, c = input("type the length for three sticks \n").split()


if int(a) + int(b) <= int(c):
    print ("trangle not possible")
else: print ("You can make a triangle!!! congrats")
