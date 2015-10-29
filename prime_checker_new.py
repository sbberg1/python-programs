# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 11:12:28 2015

@author: steveberg
"""

def prime(is_prime):
    #is_prime = input("type a number ")
    if is_prime == 2:
        print is_prime(" is a prime")
    else:
        flag = 1
        for n in range(2, is_prime - 1):
            if is_prime % n ==0:
                print is_prime,"is not a prime number"
                flag = 0
                break
        if flag == 1:
            print is_prime,"is a prime number"
            
prime()