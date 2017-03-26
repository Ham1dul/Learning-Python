# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:02:51 2017

@author: Hamidul
"""

class fraction(object):
    """ number represented as fraction"""
    def __init__(self, num, denom):
        """ initialize as number , denominatior"""
        assert type(num) == int and type(denom) == int
        self.num = num
        self.denom = denom
    def __str__(self):
        """returns fraction string"""
        return str(self.num) + '/' + str(self.denom)
    def __add__(self, other):
        """ add fraction by criss cross mult then add for top
            strait mult for bottom"""
        top = self.num * other.denom + self.denom * other.num
        bott = self.denom * other.denom
        return fraction(top,bott)
    def __sub__(self,other):
        """ sub frac by criss cross mult then add for top
            straight mult for bottom"""
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return fraction (top,bott)
    def __mul__(self,other):
        """multiplies fraction"""
        top = self.num*other.num
        bott = self.num*other.num
        return fraction(top,bott)
    def __truediv__(self,other):
        """divide self by other"""
        top = self.num*other.denom
        bott = self.denom*other.num
        return fraction(top,bott)
    def __float__(self):
        """convert number to float"""
        return self.num/self.denom
    def inverse(self):
        """num and denom"""
        return fraction(self.denom,self.num)
    
    
fraction_x = fraction(1,2)
fraction_y = fraction(1,4)
print(fraction_x) #initialize
print(fraction_y)
print(fraction_x-fraction_y) #subtract
print(fraction_x+fraction_y) #add
print(fraction_x*fraction_y) #mult
print(float(fraction_x)) #convert
print(fraction_x.inverse()) #inverse
print(fraction_x / fraction_y) #divide
        