from swampy.Lumpy import Lumpy
# create a Lumpy object
lumpy = Lumpy()
# capture reference state
lumpy.make_reference()
# run the test code
x = [1, 2, 3]
y = x
z = list(x)
# draw the current state (relative to the reference state)
lumpy.object_diagram()
