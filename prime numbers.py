# -*- coding: utf-8 -*-
"""
Created on Wed Oct 24 23:19:33 2018

@author: Haider Raheem
"""

def isprime(i):
    """ 
    input: 1, a positive integer 
    i > 1 
    returns True if i is a prime number, False otherwise 
    """
    if i > 1:  
        count = 0
        for z in range(2,i+1):
            if (i % z) == 0:
                count +=1
        if count > 1:
            return False
        if count == 1:
            return True
    else:   
        return False

def listprimes(a,b):
    """
    Lists prime numbers 
    between range a and b inclusive
    """
    for x in range(a,b+1):
        if isprime(x) :
            print(x,"is a prime number")
            
a = int(input("Enter the integer a: "))
b = int(input("Enter another positive integer b (a must be less than b): "))
if 1<a<b :
    listprimes(a,b)
else:
    print("1 <", a, "<", b, "is NOT satisfied")

