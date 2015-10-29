# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 12:20:57 2015

@author: steveberg
"""

def tax(bill):
    """Adds 8% tax to a restaurant bill."""
    bill *= 1.08					# ask Ashish
    print "With tax: %f" % bill
    return bill					# what does this do?

def tip(bill):
    """Adds 15% tip to a restaurant bill."""
    bill *= 1.15					# ask Ashish
    print "With tip: %f" % bill
    return bill					# what does this do?
    
meal_cost = 100
meal_with_tax = tax(meal_cost)
meal_with_tip = tip(meal_with_tax)