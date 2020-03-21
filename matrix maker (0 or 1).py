# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 01:22:00 2018

@author: Haider Raheem
"""
import random
def matrice(n):
    """
    input: n, a positive integer  
    prints a matrice of parameter n x n 
    random input: either 0 or 1 only as each element
    """
    for a in range(n):
        for b in range(n):
            print( random.randint(0,1), end = '\t')
        print()
    return n
    
n = int(input("Enter a positive integer: "))

matrice(n)