#!/usr/bin/env python
"""
Binary Search

This was supposed to be a binary search algorithm but it isn't working...
I used the Iterative implementation from here:
    http://en.wikipedia.org/wiki/Binary_search_algorithm
"""
from hwtools import input_nums

#creates and sorts a list from least to greatest of numbers inputted by user
nums = input_nums()
N = sorted(nums)
print "I have sorted your numbers"
print N

x = int(raw_input("Which number should I find: "))
min = int(1)
max = N[-1]

#Program finds x by reconstraining range until the midpoint equals x
while max >= min:
	mid = int((max + min) / 2)
	print "midpoint =",mid
	if x > mid:
		min = mid + 1
		print "Low"
		print "new min =",min
	elif x < mid:
		max = mid - 1
		print "High"
		print "new max =",max
	elif x == mid:
		print "Found",x,"at min =",min,"max=",max
		break
	if min >= max:	
		print "Could not find",x
		break

