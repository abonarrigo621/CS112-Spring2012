#!/usr/bin/env python
from hwtools import *

print "Section 4:  For Loops"
print "-----------------------------"

nums = input_nums()
# 1. What is the sum of all the numbers in nums?
a=sum(nums)
print "1.",a

# 2. Print every even number in nums
print "2. even numbers"
for i in range(0,len(nums)):
    if nums[i]%2 == 0:
        print nums[i]

# 3. Does nums only contain even numbers? 
only_even = False
evens=0
odds=0
#CODE GOES HERE
for i in range(0,len(nums)):
    if nums[i]%2 == 0:
        evens +=1
    else:
        odds +=1
if odds == 0:
    only_even = True
print "3.",
if only_even:
    print "only even"
else:
    print "some odd"

# 4. Generate a list every odd number less than 100. Hint: use range()
print "4.",
oddnumbers=[]
for i in range(1,101,2):
    oddnumbers.append(i)
print oddnumbers


# 5. [ADVANCED]  Multiply each element in nums by its index
print "5.", __
