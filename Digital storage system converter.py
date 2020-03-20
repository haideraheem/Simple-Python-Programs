# -*- coding: utf-8 -*-
"""
Created on Sat Oct  6 18:10:46 2018

@author: Haider Raheem
"""

x = int(input("Enter a positive integer value: "))
if x < 0 :
    print("Units must be positive")
else: 
       y= input("Enter the unit of the value (bit/byte/kilobyte): ")
       if y != "bit" and y != "byte" and y != "kilobyte":
           print("invalid unit")   
       else:
           z= input("what unit do you want (bit/byte/kilobyte): ")
           if z != "bit" and z != "byte" and z != "kilobyte":
              print('invalid conversion unit')

       if y == "bit" and z == "bit":
           print(x, y, "is equal to", x, z)
       elif y == "bit" and z == "byte":
           print(x, y, "is equal to", x/8, z)
       elif y== "bit" and z == "kilobyte":
           print(x, y, "is equal to", (x/8)/1024, z)
       elif y== "byte" and z == "bit":
           print(x, y, "is equal to", x*8, z)    
       elif y== "byte" and z == "byte":
           print(x, y, "is equal to", x, z)      
       elif y== "byte" and z == "kilobyte":
           print(x, y, "is equal to", x/1024, z)        
       elif y== "kilobyte" and z == "bit":
           print(x, y, "is equal to", (x*1024)*8, z)           
       elif y== "kilobyte" and z == "byte":
           print(x, y, "is equal to", x*1024, z)
       elif y== "kilobyte" and z == "kilobyte":
           print(x, y, "is equal to", x, z)
          