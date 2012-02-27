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

<<<<<<< HEAD
def greeter(name):  
    name = str(name).lower()
    print "hello,",name

=======
# def greeter(name):
>>>>>>> 3205ce588d6ab68eff8ce1e79725079c03bbb0bd


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

<<<<<<< HEAD
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


    


=======
# def box(w,h):



# ADVANCED
# Draw a Festive Tree
#    draw a festive tree based on the specifications.  You will need to discover the arguments 
#    and behavior by running the unittests to see where it fails.  Return a string, do not print.
#
#  ex:
#    >>> print tree()
#        *
#        ^
#       ^-^
#      ^-^-^
#     ^-^-^-^
#    ^-^-^-^-^
#       | |
#       | |

# def tree()
>>>>>>> 3205ce588d6ab68eff8ce1e79725079c03bbb0bd

