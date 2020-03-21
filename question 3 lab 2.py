# -*- coding: utf-8 -*-
"""9
Created on Mon Oct 15 08:42:49 2018

@author: Haider Raheem
"""

x = 0
while x == 1 or x == 0:  
    x = int(input("Enter an integer (except 0 and 1): "))
x =x**30  
j = 0
i = 0
count = 0

for i in range(-x,x) or range(x, -x):
    for j in range(2,9):
        if i ** j == x:
            print (x, "=", i, "**", j)
            count +=1
if count == 0:
    print("There is no such (i,j) integer pair so that i ** j is equal to your integer", x, "where 2 <= j <= 8.")           