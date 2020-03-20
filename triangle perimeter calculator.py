# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 00:43:08 2018

@author: Haider Raheem
"""

print("Triangle Perimeter Calculator")
x = float(input("Enter the first edge: "))
y = float(input("Enter the second edge: "))
z = float(input("Enter the third edge: "))
print(" ")
if x+y>=z and x+z>=y and y+z>=x:
    print("Edges "+str(x)+","+str(y)+", and "+str(z)+" form a valid triangle")
    print(" ")
    print("The perimeter is", x+y+z)
else:
    print("Edges "+str(x)+","+str(y)+", and "+str(z)+" don't form a valid triangle")