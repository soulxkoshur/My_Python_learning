from swampy.TurtleWorld import *
import math

world = TurtleWorld()
t = Turtle()

def polygon(x, n, length):
    angle = 360.0 / n
    for i in range(n):
        fd(x, length)
        lt(x, angle)

polygon(t, 6, 100)



wait_for_user()

