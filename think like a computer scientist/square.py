from swampy.TurtleWorld import *

world = TurtleWorld()
t = Turtle()

def square(x, length):
    print (x)
    for i in range(4):
        fd(x, length)
        lt(x)
square(t, 400)

wait_for_user()

