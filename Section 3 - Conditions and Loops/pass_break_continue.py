counter=0
while counter<100:
    if counter == 4:
        break
    else:
        pass
    print(counter)
    counter+=1

print("")

for i in "Python":
    if i =="h":
        continue # all the other code are not considered
    print(i)

print("")

for i in range(0,5):
    if i<2:
        continue
    print(i)