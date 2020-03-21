# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 14:20:08 2018

@author: haider.raheem-ug
"""

import random
import matplotlib.pyplot as plt

numberofparticles = int(input("Enter number of particles: "))
nofsteps = int(input("Enter number of steps: "))
prob = float(input("Enter the probability of going right: "))

def move(n_steps, prob):
    for i in range(n_steps):
        npos = 0
        for i in range(n_steps):  
            x = takeStep(prob)
            npos += x
        return npos
        
    
def takeStep(prob):
    stepChoices =[]
    for i in range(int(10*prob)):
        stepChoices.append(1)
        
    for i in range(int(10-(10*prob))):
        stepChoices.append(-1)
        
    return random.choice(stepChoices)



fp = []
sumfp = 0
avg = 0
for i in range(numberofparticles):
    fp.append(move(nofsteps, prob))
for i in range(len(fp)):
    sumfp += fp[i]
    
average = sumfp/numberofparticles
print("mean: {:.2f}  ".format(average))
plt.clf()
plt.plot(fp, "ro")
plt.ylabel("final position")
plt.xlabel("Practice index")
plt.title("Final positions of " + str(numberofparticles) + " particles in " +  str(nofsteps) +" prob(going right) =  " + str(prob))
plt.figure()
plt.hist(fp)
plt.xlabel("particle final position")
plt.ylabel("count of particles")
plt.title("Histogram of Final positions of " + str(numberofparticles) + " particles in " +  str(nofsteps) +" steps")
