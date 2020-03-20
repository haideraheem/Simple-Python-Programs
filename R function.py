# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:11:11 2018

@author: Haider Raheem
"""

a= float(input("Type a : "))
b= float(input("Type b : "))
c= float(input("Type c : "))
x= (a*b)+(b*c)+(c*a)
y= (a+b+c)
r= x/y 
print( )
print("The result of the calculation is {0:.2f}".format(r))