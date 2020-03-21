# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 05:38:13 2018

@author: Haider Raheem
"""

valid= True
x= int(input("Enter lower bound: "))
y= int(input("Enter upper bound: "))
c = 0
c2 = 0
total =0
if y < x:
    print("Invalid range")
    valid=False   
else:
    for i in range(x, y+1, 1 ):
        i/7
        if i%7 == 0 :
            c += 1
            i/5
            if i%5 == 0:
                c2 += 1
            else:  
                total= total+i       
t = c-c2                
if t != 0 :               
    print(t, "values are divisible by 7 but not 5 between", x, "and", y,
    "inclusive")
    print("Average Value: {0:.1f}".format (total/t))
elif t == 0 and valid :
    print( "there are no such values that are disvisible by 7 but not 5" )    
            