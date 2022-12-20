from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot  as plt
import numpy as np
import time

fig = plt.figure()

chart = fig.add_subplot(1,1,1,projection='3d')
x,y,z = [1,2,3,4,5,6,7,8,9,10],[2,3,4,5,1,6,2,1,7,2],[0,0,0,0,0,0,0,0,0,0] # z é zero pq se nao o bloco fica flutuando

dx = np.ones(10) # largura das barras
dy = np.ones(10) # commprimento das barras
dz = [1,2,11,4,5,6,7,8,9,10] # tamanho das barras

chart.bar3d(x,y,z,dx,dy,dz, color = 'cyan')

chart.set_xlabel('X label')
chart.set_ylabel('Y label')
chart.set_zlabel('Z label')


plt.show()
#time.sleep(3)