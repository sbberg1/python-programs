# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:16:18 2015

@author: steveberg
"""

# For loop w/ .append() and .sort()

start_list = [5, 3, 1, 2, 4]
square_list = []

for x in start_list:
    x = x ** 2
    square_list.append(x)
    square_list.sort()

print square_list