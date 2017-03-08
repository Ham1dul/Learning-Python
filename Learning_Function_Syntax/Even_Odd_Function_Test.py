# -*- coding: utf-8 -*-
"""
Created on Wed Mar  8 09:18:31 2017

TESTING FUNCTION SYNTAX

odd or even

@author: Hamidul
"""

def is_even(x):
    """
    takes an integer input
    outputs true if int is even
    else outputs false
    
    """
    return x%2==0


def is_odd(x):
    """
    
    takes integer input
    outputs true if in is odd
    else outputs false
    
    """
    return x%2==1


y=int(input('input an integer\n'))
print('is interger odd?')
print(is_odd(y))
print('is interger even?')
print(is_even(y))