#!/usr/bin/env python
"""
rects.py

Pygame Rectangles
=========================================================
The following section will test your knowledge of how to 
use pygame Rect, arguably pygame's best feature. Define
the following functions and test to make sure they 
work with `python run_tests.py`

Make sure to use the documentation 
http://www.pygame.org/docs/ref/rect.html


Terms:
---------------------------------------------------------
  Point:     an x,y value
               ex:  pt = 3,4

  Polygon:   a shape defined by a list of points
               ex:  poly = [ (1,2), (4,8), (0,3) ]

  Rectangle:  pygame.Rect
"""

from pygame import Rect

# 1. poly_in_rect
#      Check to see if the polygon is completely within a given 
#      rectangle.
#
#      returns:  True or False

def poly_in_rect(poly, rect):
    inside = 1
    for pt in poly:
        inside *= rect.collidepoint(pt)
    # if rect.collidpoint returns false inside returns to 0 so poly is not inside otherwise inside = 1 and poly is inside
    return inside

# 2. surround_poly
#      Create a rectangle which contains the given polygon.  
#      It should return the smallest possible rectangle 
#      where poly_in_rect returns True.
#
#      returns:  pygame.Rect

def surround_poly(poly):
    xmin, ymin = xmax, ymax = poly[0]
    for pt in poly:
        x,y = pt
        #change dimensions of rectangles so they equal points of poly
        if x <= xmin:
            xmin = x
        if x >= xmax:
            xmax = x
        if y <= ymin:
            ymin = y
        if y >= ymax:
            ymax = y
    return Rect(xmin,ymin,(xmax-xmin+1),(ymax-ymin+1))

