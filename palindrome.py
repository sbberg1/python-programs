# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 10:36:58 2015

@author: steveberg
"""

def main():
    list_from_user = []	        # Create an empty list
    list_from_user_reverse = [] #Create second list to create reverse
    max_value = 0  	    # set the maximum value of list_from_user to 0
    max_counter = 0  	    # set the count of maximum value to 0
    position_counter = 0    # figure out position of max_value
    flag = 0                # to stop position_counter from increasing after first max_value
    list_size = input("How many numbers in your list?")  # number of inputs
    counter_for_reverse = list_size-1
    counter_for_reverse_2 = list_size-1
    counter_for_forward = 0
    for n in range(list_size):
        input_variable = input("Enter number")
        list_from_user.append(input_variable)
    for n in range (list_size):
        list_from_user_reverse.append(list_from_user[counter_for_reverse])
        counter_for_reverse = counter_for_reverse-1
    for n in range (list_size):
        if list_from_user[counter_for_forward] == list_from_user[counter_for_reverse_2]:
            counter_for_forward = counter_for_forward+1
            counter_for_reverse_2 = counter_for_reverse_2-1
        else:
            flag = flag+1
            break
    if flag == 0:
        print "this is a palindrome"
    else:
        print "this is not a palindrome"
if __name__ == "__main__":
    main()