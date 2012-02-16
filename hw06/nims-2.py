#!/usr/bin/env python
"""nims.py

A simple competitive game where players take stones from stone piles.
"""

#Defines initial number of stones in pile and creates variables for each player to choose stones
numberofstones = 40
a = 0
b = 0
numberofstones = int(numberofstones)
a = int(a)
b = int(b)

#Player 1 and 2 loop
while numberofstones >= 0:
#Allows player 1 to choose a quantity of 1-5 stones
	print numberofstones,"stones left. Player 1 [1-5]: "
    a = raw_input()
#If Player 1 chooses a quantity of stones greater than 5 they are prompted to choose again    
	while int(a) > 5:
        print numberofstones,"stones left. Player 1 [1-5]: "
        a = raw_input()
#If Player 1 chooses a quantity of stones greater than the amount left in the pile, then it prints Not Enough Stones, and they are prompted to choose again.
	while int(a) > int(numberofstones):
        print "Not enough stones."
        print numberofstones,"stones left. Player 1 [1-5]: "
        a = raw_input()
#Prints "Player 2 wins" if Player 1 takes last stone otherwise it adjusts the number of stones left according to the quantity Player 1 took. 
	if int(numberofstones) - int(a) == 0:
        print "Player 2 wins!!!"
        break
    numberofstones = int(numberofstones) - int(a)
#Player 2's turn each line corresponds to the same line for player 1. 
	print numberofstones,"stones left. Player 2 [1-5]: "
    b = raw_input()
    while int(b) > 5:
        print numberofstones,"stones left. Player 2 [1-5]: "
        b = raw_input()
    while int(b) > int(numberofstones):
        print "Not enough stones."
        print numberofstones,"stones left. Player 2 [1-5]: "
        b = raw_input()
    if int(numberofstones) - int(b) == 0:
        print "Player 1 wins!!!"
        break
    numberofstones = int(numberofstones) - int(b)




