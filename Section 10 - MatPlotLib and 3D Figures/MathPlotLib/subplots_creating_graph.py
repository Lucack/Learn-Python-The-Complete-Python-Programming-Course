import matplotlib.pyplot as plt
fig = plt.figure()

rect = fig.patch
rect.set_facecolor('green')

x = [3,7,5,8]
y = [5,13,2,8]


graph1 = fig.add_subplot(1,1,1,facecolor='black') # ( how big , how big , how many graphs gona be)
graph1.plot(x,y,'red', linewidth = 4.0)

    # more colors

    # pontos nos eixos --> white
graph1.tick_params(axis="x",color="white")
graph1.tick_params(axis="y",color="white")

    # borda do grafico, cores dos eixos xy --> white ('w')
graph1.spines["top"].set_color('w')
graph1.spines["left"].set_color('w')
graph1.spines["right"].set_color('w')
graph1.spines["bottom"].set_color('w')

graph1.set_title('Random graph', color='white')
graph1.set_xlabel("This is the x axis", color='white')
graph1.set_ylabel("This is the y axis", color='white')




plt.show()
