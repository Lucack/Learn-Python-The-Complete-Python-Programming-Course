import matplotlib.pyplot as plt
fig = plt.figure()

rect = fig.patch
rect.set_facecolor('green')

x = [3,7,5,8]
y = [5,13,2,8]

x2 = [0,4,7,10]
y2 = [3,7,1,12]

x3 = [2,4,6,8]
y3 = [13,5,8,2]


graph1 = fig.add_subplot(2,1,1,facecolor='black')
graph1.plot(x,y,'red', linewidth = 2.0)

graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis="y",color="white")

graph1.spines["top"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')

graph1.set_title('Random graph', color='white')
graph1.set_xlabel("This is the x axis", color='white')
graph1.set_ylabel("This is the y axis", color='white')

# -------------------- #

graph2 = fig.add_subplot(2,1,2,facecolor='black')
graph2.plot(x2,y2,'yellow', linewidth = 2.0)



graph2.tick_params(axis="x",color="white")
graph2.tick_params(axis="y",color="white")

graph2.spines["top"].set_color('w')
graph2.spines["left"].set_color('w')
graph2.spines["right"].set_color('w')
graph2.spines["bottom"].set_color('w')

graph2.set_title('Random graph', color='white')
graph2.set_xlabel("This is the x axis", color='white')
graph2.set_ylabel("This is the y axis", color='white')


plt.show()

