import matplotlib.pyplot as plt
import numpy as np
pos = np.arange(6) + 0.5
print(pos) # [0.5 1.5 2.5 3.5 4.5 5.5] for example 0.5 is a distance of bars

students = ["Avi", "Jose","Bob","Nick","Zelda","Matt"]

plt.barh(pos,(4,8,12,3,17,6), align='center',color = 'red')

plt.xlabel('Height in Inches', color='Red')
plt.ylabel('Students', color='r')
plt.title('Height of Students in Inches', color='Black')


plt.tick_params(axis='x', colors='w')
plt.tick_params(axis='y', colors='w')

    #y.ticks coloca legenda direta no eixo
plt.yticks()

    # ajusts

plt.subplots_adjust(left = .11, bottom= .12 , right=.94)
plt.show()
