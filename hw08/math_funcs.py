#!/usr/bin/env python

import math

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

<<<<<<< HEAD
def distance(a,b):
    x1, y1 = a
    x2, y2 = b
    distance = math.sqrt(((x2-x1))**2 + ((y2-y1)**2))
    return distance


=======
# def distance(a, b):
>>>>>>> 3205ce588d6ab68eff8ce1e79725079c03bbb0bd


# ADVANCED
# Normalizing Vectors
#   normalize a vector of length N.  If given all zeros, just spit back the same vector
#   http://www.fundza.com/vectors/normalize/index.html

#   ex:
#     >>> normalize((1,1))
#     [0.70710678118654746, 0.70710678118654746]
#     >>> normalize([0,0,0])
#     [0,0,0]
#     >>> normalize([1,1,1,1])
#     [0.25, 0.25, 0.25, 0.25]

# def normalize(vec):
