# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:20:08 2015

@author: steveberg
"""
# another dictionary example

menu = {}                       # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
menu['Chicken Parm'] = 12.50
menu['Chicken Wings'] = 8.50
menu['Chicken Breast'] = 10.50

print menu['Chicken Alfredo']                               #prints the value
print "There are " + str(len(menu)) + " items on the menu."  #what is str()?
print menu                                  # prints the whole dictionary