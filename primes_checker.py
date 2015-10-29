# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 13:56:17 2015

@author: steveberg
"""

def prime():
    list_from_user = []
    primes_below_two = 2
    list_size = input("How many numbers in your list? ")
    counter_to_test_primes = list_size - 1
    for n in range(list_size):
        input_variable = input("Enter number ")
        list_from_user.append(input_variable)
    for n in range(list_size):
        while list_from_user[counter_to_test_primes] > primes_below_two:
            if list_from_user[counter_to_test_primes]%2 == 0 and list_from_user[counter_to_test_primes] != primes_below_two:
                print list_from_user[counter_to_test_primes], (" is not a prime")
            else:
                print list_from_user[counter_to_test_primes], (" is a prime")
        counter_to_test_primes = counter_to_test_primes - 1
print ("This is a prime number checker.")

prime()