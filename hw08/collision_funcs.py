#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

<<<<<<< HEAD
def point_in_box(pt, box):
    a, b = pt
    x, y, w, h = box
    if a >= x and a < x+w and b >= y and b < y+h:
        return True
    else: 
        return False
         



=======
# def point_in_box(pt, box):
>>>>>>> 3205ce588d6ab68eff8ce1e79725079c03bbb0bd

