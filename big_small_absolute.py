# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:40:28 2015

@author: steveberg
"""

def biggest_number(*args):		#(*args) ??  How does it know to choose all 4?
    print max(args)
    return max(args)			# how come the return is after the print?
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)