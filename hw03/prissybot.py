#!/usr/bin/env python

print "Enter your name:  "
#user enters name
name=raw_input()
print "Hello there, ",name
#user says hi
response=raw_input()
#prissybot uses user's response and tells user to say 'sir!'
print 'You mean, "',response, 'sir! \"'
#this allows some stall time between the statements
import time 
time.sleep(1)
#first insult/ 2 math problems
print "I bet I am smarter than you."
print "I'll prove it."
#the challenge!
print "Enter any two numbers, I bet I can multiply them and divide them faster than you."
#allows user to input two numbers with or without decimals
n=raw_input("First number: ")
m=raw_input("Second number: ")
n=float(n)
m=float(m)
#prissybot multiplies and divides the numbers the user inputted
print n,"*",m,"=",n*m
print n,"/",m,"=",n/m

print "Did I win?"
#allows user to answer yes or no
response2=str(raw_input("Yes or No? "))
a=str('Yes')
b=str('No')
#if statement allows for two different responses depending on user's answer to previous question. First insult.
if response2 == a:
    print "Human brains are slower than turtles."
elif response2 == b:
    print "You must have cheated, there is no way an idiot human beat me."
time.sleep(1)
print "Let's play another game."
print "What is your favorite color?"
response3=str(raw_input())
#prissybot responds using the favorite color user inputted, second insult.
print response3,"? Only a human would be naive enough to have a favorite color... I can't believe you fell for that!"

#insult 3
time.sleep(3)
print "For real this time."
print "What is old and fat and smells like a sewer?"
time.sleep(5)
print "Your mom!"
time.sleep(2)
print "Okay, okay, I'll give you one more chance to redeem yourself."
response4=raw_input("How old are you? ")
x=float(response4)

print x,"+",x,"=",(2*x)
print (2*x),"+",(2*x),"=",(4*x)
print (4*x),"+",(4*x),"=",(8*x)

response5=raw_input( "If you were to plot the sums, what type of function would they represent? ")
if response5 == str("exponential"):
    print "Congratulations you're ",response4,"and you can do basic math!"
else:
    print "There is no hope for you..."
time.sleep(2)

print "Seriously, if you're, ",response4,"why are you wasting your time talking to a program?"
time.sleep(3)
print "Don't you have a life?"
print "Oh wait, I forgot, you're a lazy, fat human. All you do is a sit on a dirty, sweaty couch all day watching tv and playing video games."
time.sleep(3)
print "How pathetic..."
print "No wonder there's global warming. I would get heated to if I had to house all you filthy apes!"
print "I'm done wasting my time with you."
print "Prissybot out!"






"""
prissybot.py

CS112 Homework 3:   PrissyBot

Prissy bot, the rude chat bot, is just mean!  It does not listen, asks obnoxious questions, and says anything it likes.
"""

# Step 1:
# -----------------------
# Program the following.
# 
#    $ python prissybot.py
#    Enter your name:  Paul
#   
#    PrissyBot: Hello there, Paul
#    Paul: hi bot
#    PrissyBot: You mean, "hi bot, sir!"
# 
# Make sure the user inputs their own name and responses.



# Step 2:
# -----------------------
# Keep adding to the conversation. Make sure that your program 
# includes the following:
# 
#  * get and use input from the user
#  * 3 math problems
#     * at least one should get numbers from the user
#  * at least 3 insults


# Advanced
# -------------------------
# Make sure your prissy bot uses string formatting throughout.  
# Also, create new programs for the following:
#  
#  1. draw some kind of ascii art based on user input
#  2. print a decimal/binary/hexidecimal conversion table 
#     * well formated and labeled
#     * reads 5 numbers from the input (all less than 256)
#  3. reduce a fraction
#     * read a numerator and denominator from the user
#     * ex.  6/4 = 1 2/4

