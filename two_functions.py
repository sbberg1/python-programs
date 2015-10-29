# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:25:03 2015

@author: steveberg
"""

def one_good_turn(n): 		# 1st function
    return n + 1
    
def deserves_another(n):  		#2nd function that calls the first
    return one_good_turn(n) + 2