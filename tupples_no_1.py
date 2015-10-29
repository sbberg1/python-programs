# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 10:23:14 2015

@author: steveberg
"""

def pairs():
    max_value = 0
    magic_sum_counter = 0
    list_from_user = []	                                                    # Create an empty list to store user input numbers
    sum_of_the_pairs = []	                                                    # Create an empty list to store sums of paired numbers
    list_size = input("How many numbers in your list? ")                        # Number of inputs

    for n in range(list_size):                                                  # User enters numbers
        input_variable = input("Enter number ")
        list_from_user.append(input_variable)                                   # Populate list with user entered numbers

    magic_sum = input("What paired number sum should I look for? ")              # Value of sum to search for

    for n in range(list_size):
        for i in range(n + 1, list_size):
            if magic_sum == list_from_user[n] + list_from_user[i]:
                magic_sum_counter = magic_sum_counter + 1
        sum_of_the_pairs.append(list_from_user[n] + list_from_user[i])
        
    for n in range(len(sum_of_the_pairs)):
        if sum_of_the_pairs[n] >= max_value:
            max_value = sum_of_the_pairs[n]

    print "The numbers of pairs that sum to ", magic_sum, "is ", magic_sum_counter
    print "The maximum value of the pairs summed is ", max_value
            
pairs()
