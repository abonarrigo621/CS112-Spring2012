#!/usr/bin/env python
"""
Selection sort

This is my selection sort, it's not working right!!!
I used this:
    http://en.wikipedia.org/wiki/Selection_sort
"""
from hwtools import input_nums

nums = input_nums()

print "Before sort:"
print nums

#Sorts nums from least to greatest
N=len(nums)
for x in range(N):
    p=int(x)
    for i in range(x+1, N):
        while nums[i] < nums[p]:
			pos=i
			nums[i],nums[p]=nums[p],nums[i]

print "After sort:"
print nums
