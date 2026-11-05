# here we define the main variables and import tools that we would need to draw a circle using the turtle.

from swampy.TurtleWorld import *
import math

world = TurtleWorld()
t = Turtle()
t.delay = 0.01 # this makes the turtle faster as, i used it because the default speed was too slow to draw a circle.

# here we define our first fuction, this is a polygon, and it has a loop fuction built into it so i don't have to wrtie manually for the turtle to turn and by how much length
def polygon (x, n, length):
   
    for i in range(n):
        angle = 360.0 / n
        fd(x, length)
        lt(x, angle)

 ### here we define the circle, in it we call the polygon fuction already written with loop, so we don't have to do that agian in the circle       

def circle( x, r):
    c = 2 * math.pi * r
    n = 50
    length = c / n
    polygon (x, n, length)

## this is the most important part, whatever function i call here, becomes the output, if i call the polygon fuction with the values i put in i won't see a circle but a polygon. i can technically make a circle with just the polygon fuction but it would not look elegant.
#polygon (t, 100, 5)

## above is the example, by not calling the circle function i defined i can still make circle but I would not be able to control the radius!!

circle(t, 100)
wait_for_user()


