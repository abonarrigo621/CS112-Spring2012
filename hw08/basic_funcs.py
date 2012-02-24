#!/usr/bin/env python

# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

def greeter(name):  
    name = str(name).lower()
    print "hello,",name



# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

def box(w,h):
    if w < 1 or h < 1 or type(w) != int or type(h) != int:
        print "Error: Invalid Dimensions"
        return

    if w == 1:
        top = "+"
    else:    
        top = "+" + ((w-2) * "-") + "+" 
    sides = "|" + ((w-2) * " ") + "|"
    print top
    for i in range(h-2):
        print sides
    if w > 1 and h > 1:
        print top


    



