# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 20:40:45 2017

@author: Hamidul
"""

class coordinate(object):
    def __init__(self,x,y):
        """input 2 integers to map the x and y locations
        in the coordinate plane to x and y of the object"""
        self.x = x
        self.y = y
    def distance(self,other):
        x_diff_sq=(self.x - other.x)**2
        y_diff_sq=(self.x - other.x)**2
        return (x_diff_sq + y_diff_sq)**.5
    def __str__(self):
       return '<'+str(self.x)+','+str(self.y)+'>' 
        
        
c = coordinate(5,5)
origin = coordinate(0,0) #initiate
print(c.y)  #show value inside class
print(origin.x) #show value in class
print(origin.distance(c))   #use eular distance formula
print(c)    #use __str__ speical def to print object
print(type(c))   # <class __main__.coordinate> type of object
print(type(coordinate)) #a class is a type object
print(isinstance(c,coordinate)) #checks whether its in the class
