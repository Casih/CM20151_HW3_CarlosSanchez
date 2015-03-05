
# coding: utf-8

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time 
L = []
Dir = "/Users/Carlos/MetodosComputacionales/tareas/HW3/Punto3/Test"
for file in os.listdir("/Users/Carlos/MetodosComputacionales/tareas/HW3/Punto3/Test"): # Por favor cambien la direccion por la direccion donde tengan los .txt para que sirva. 
    if file.endswith(".txt"):
        L.append(file)

col1 = []
col2 = []
Dir = "/Users/Carlos/MetodosComputacionales/tareas/HW3/Punto3/Test"
for file in L:
    a = np.genfromtxt(os.path.join(Dir,file),usecols = (0))
    b = np.genfromtxt(os.path.join(Dir,file),usecols = (1))
    col1.append(a)
    col2.append(b)

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
def animate(i):
    x = col1[i]
    y = col2[i]
    ax1.clear()
    ax1.scatter(x,y)
anim = animation.FuncAnimation(fig, animate, interval=50)
plt.show()



