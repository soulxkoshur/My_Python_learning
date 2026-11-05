from swampy.TurtleWorld import *
import math

world = TurtleWorld()
t = Turtle()
t.delay = 0.04
def polyline(x, n, length, angle):
    for i in range(n):
        fd(t, length)
        lt(t, angle)


def polygon(x, n, length):
    angle = 360.0 / n
    polyline(x, n, length, angle)

def arc(x, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = float(angle) / n
    polyline(x, n, step_length, step_angle)

def circle(x, r):
    arc(t, r, 360)
arc(t, 100, 270)
wait_for_user()

