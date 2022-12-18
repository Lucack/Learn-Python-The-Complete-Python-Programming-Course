import matplotlib.pyplot as plt

x=[]
y=[]

readFile = open('Section 10 - MatPlotLib and 3D Figures\point_graph.txt','r')
data = readFile.read().split("\n")
print(data)

for i in data:
    var = i.split(",")
    x.append(int(var[0]))
    y.append(int(var[1]))
 
plt.plot(x,y)
plt.show()
