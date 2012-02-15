#!/usr/bin/env python

from random import randint

s = 1
input_number = int(raw_input())
number_list = [ ]

#adds random integers to list so that list length equals input number and includes input number
for _ in range(input_number):
    number_list.append(randint(0,20))
print number_list

while s:
    s = 0
    for i in range(1,input_number):
        if number_list[i-1] > number_list[i]:
            t1 = number_list[i-1]
            t2 = number_list[i]
            number_list[i-1] = t2
            number_list[i] = t1
            s = 1

print number_list
