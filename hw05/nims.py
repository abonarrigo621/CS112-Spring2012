#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

numberofstones=40
a=0
b=0
numberofstones=int(numberofstones)
a=int(a)
b=int(b)


while numberofstones>=0:
    print numberofstones,"stones left. Player 1 [1-5]: "
    a=raw_input()
    while int(a)>5:
        print numberofstones,"stones left. Player 1 [1-5]: "
        a=raw_input()
    while int(a)>int(numberofstones):
        print "Not enough stones."
        print numberofstones,"stones left. Player 1 [1-5]: "
        a=raw_input()
    if int(numberofstones) - int(a) == 0:
        print "Player 2 wins!!!"
        break
    numberofstones=int(numberofstones)-int(a)
    print numberofstones,"stones left. Player 2 [1-5]: "
    b=raw_input()
    while int(b)>5:
        print numberofstones,"stones left. Player 2 [1-5]: "
        b=raw_input()
    while int(b)>int(numberofstones):
        print "Not enough stones."
        print numberofstones,"stones left. Player 2 [1-5]: "
        b=raw_input()
    if int(numberofstones) - int(b) == 0:
        print "Player 1 wins!!!"
        break
    numberofstones=int(numberofstones)-int(b)




