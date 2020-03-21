# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 0
y = 0
while y != "" and x != "" :
    x = (input("enter first string:"))
    y = (input("enter second string:"))
    z = str(x[-len(y):])
    v = str(y[-len(x):])
    if y != "" and x != "" : 
        if z.lower() == y.lower():
            print("string 2 is at the end of string 1")
        elif v.lower() == x.lower():
            print("string 1 is at the end of string 2")
        else :
            print("String 1 and String 2 do not end with the other")
       

if x == "" and y =="":
    print("Both strings are empty, goodbye.")
elif x == "":
   print("first string is empty, goodbye.")
elif y== "":
   print("Second string is empty, goodbye.")