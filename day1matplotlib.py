# -*- coding: utf-8 -*-
"""day1matplotlib

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1sm2MjLerEmweCk1RYZThPSN6TQ3zMUbK
"""

import matplotlib
dir(matplotlib)
del matplotlib

import matplotlib.pyplot as plt
x=[1,2]
y=[3,4]
plt.xlabel("time")
plt.ylabel("dist")
plt.plot(x,y,label="sand")
plt.bar(x,y,label='run')
plt.grid(color='green')
x=[2,3]
y=[4,3]
plt.plot(x,y,label='water')
plt.legend()

plt.xlim(0,5)
plt.ylim(3,5)
#plt.show(x,y)