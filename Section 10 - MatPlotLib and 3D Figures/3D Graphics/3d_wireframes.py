from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot  as plt
import numpy as np
import time

fig = plt.figure()

chart = fig.add_subplot(1,1,1,projection='3d')

x,y,z = axes3d.get_test_data(0.05)
chart.plot_wireframe(x,y,z,rstride=4,cstride=4)

chart.set_xlabel('X label')
chart.set_ylabel('Y label')
chart.set_zlabel('Z label')


plt.show()
#time.sleep(3)