# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 13:53:18 2018

@author: haider.raheem-ug
"""

import numpy as np
import matplotlib.pyplot as plt
plt.clf()

x = np.linspace(-2*np.pi, 2*np.pi, 51)

y1= np.sin(x)
y2= np.cos(x)

plt.plot(x, y1, "r*--", label = "sin(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.plot(x, y2, "b:", label = "cos(x)")
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.grid('on')
plt.xlim(-2*np.pi, 2*np.pi)
plt.ylim(-1,1)