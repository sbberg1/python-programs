# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:35:34 2015

@author: steveberg

Instructions:

1.	First, def a function called cube that takes an argument called number. Don't forget the parentheses and the colon!
2.	Make that function return the cube of that number (i.e. that number multiplied by itself and multiplied by itself once again).
3.	Define a second function called by_three that takes an argument called number.
4.	If that number is divisible by 3, by_three should call cube(number) and return its result. Otherwise, by_three should return False


"""

def cube(number):
    number = number**3
    return number
    
def by_three(number):
    if number % 3 == 0:
        print "divisable by three"  
        return cube(number)  
    else:
        print "not divisible by three"
        
by_three(cube(9))
print cube(9)