# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 17:31:28 2018

@author: Haider Raheem
This program takes three integer inputs and then sorts them from highest to lowest and gives a string as output
"""

x= int(input("Enter the first integer: "))
y= int(input("Enter the second integer: "))
z= int(input("Enter the third integer: "))
if x<=y and x<=z and y<=z:
     print("The sorted nums are", x, y, z)
elif y<=z and y<=x and z<=x:
     print("The sorted nums are", y, z, x)    
elif z<=x and z<=y and x<=y:
     print("The sorted nums are", z, x, y)
elif z<=y and z<=x and y<=x:
     print("The sorted nums are", z, y, x)
elif x<=z and x<=y and z<=y:
     print("The sorted nums are", x, z, y)    
elif y<=x and y<=z and x<=z:
     print("The sorted nums are", y, x, z)
