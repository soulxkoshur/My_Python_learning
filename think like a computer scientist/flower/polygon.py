from swampy.TurtleWorld import *
import math

world = TurtleWorld()
t = Turtle()
t.delay = 0.001
def polyline (x, n, length, angle):
      for i in range (n):
        fd(x, length)
        lt(x, angle)
def polygon (x, n, length):
    angle = 360.0 / n
    polyline(x, n, length, angle)
def arc (x, r, angle):
    arclength = 2 * math.pi * r * angle / 360
    n = int(arclength / 2)
    step_length = arclength / n
    step_angle = float(angle) / n
    polyline (x, n, step_length, step_angle)
def circle(t, r):
    arc(t, r, 360)

wait_for_user
    


