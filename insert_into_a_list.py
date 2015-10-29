# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:08:26 2015

@author: steveberg
"""
# how to insert something into a list
# using .index
# using .insert

animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")

animals.insert(duck_index, "cobra")

print animals # Observe what prints before the insert operation