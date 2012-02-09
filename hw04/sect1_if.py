#!/usr/bin/env python
from hwtools import *

print "Section 1:  If Statements"
print "-----------------------------"

# 1.  Is n even or odd?
n = raw_input("Enter a number: ")
n = int(n)

if n%2 == 0:
    print "1. ",n,"is even."
else:
    print "1. ",n,"is odd."

# 2. If n is odd, double it
if n%2 == 1:
    print "2. ",2*n
else:
    print "2. ",n

# 3. If n is evenly divisible by 3, add four
if n%3 == 0:
    print "3. ",n+4
else:
    print "3. ",n


# 4. What is grade's letter value (eg. 90-100)
grade = raw_input("Enter a grade [0-100]: ")
grade = int(grade)

if 90<= grade<=100:
    print "4. A"
elif 80<=grade<=89:
    print "4. B"
elif 75<=grade<=79:
    print "4. C"
elif 65<=grade<=74:
    print "4. D"
elif 0<=grade<=64:
    print "4. F"






