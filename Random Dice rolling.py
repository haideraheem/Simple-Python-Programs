# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 00:16:05 2018

@author: Haider Raheem
"""
import random

def throwUntil(x):
    """
    input sum: x, 2<=x<=12
    random input for  die1 and die2 rolled
    counts time rolled to get sum
    """
    count = 0
    die1 = 0
    die2 = 0
    while die1 + die2 != x:
        die1 = random.randint(1, 6) 
        die2 = random.randint(1, 6)
        count +=1
    print("Dice are rolled", count, "times to get the sum", x)
    
x = 0
while x<2 or x>12:
    x = int(input("Enter sum of dice: "))
    if x<2 or x>12:
        print("Sum must be between 2 and 12 inclusive")   

throwUntil(x)