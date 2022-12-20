import matplotlib.pyplot as plt
import numpy as np
import time

sizes = [50,23,7,15,5]
plt.pie(sizes)

    #colors

colors = ["orange","cyan","black","red","magenta"]

    # labels / legends

labels = ["Android","Windows", "Apple","Ubuntu","Xiaomi"]
plt.legend(title = "Legend")

    # title

plt.title("Pie Chart")
plt.legend(title = "Legend", loc = "lower left", labels=labels)


plt.pie(sizes, colors=colors, startangle=90, labels=labels)
plt.axis('equal')

plt.show()
time.sleep(3)