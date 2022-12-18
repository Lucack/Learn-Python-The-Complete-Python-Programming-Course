import matplotlib.pyplot as plt
import numpy as np
pos = np.arange(6) + 0.5
print(pos) # [0.5 1.5 2.5 3.5 4.5 5.5] for example 0.5 is a distance of bars

plt.barh(pos,(4,8,12,3,17,6), align='center',color = 'red')
plt.show()
