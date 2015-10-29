# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:38:36 2015

@author: steveberg
"""

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function(range(3))