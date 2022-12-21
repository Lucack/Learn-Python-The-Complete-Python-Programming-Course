import pandas as pd
a=[10,"Namaste",23.5,"Hello"]
df = pd.Series(a, index = ["a","b","c","d"])
print(df)
print(df[0])
print(df[1])

d = {"Seatle":1000000,"San Francisco":500000,"San Jose":1500000}
cities = pd.Series(data = d)
print(cities)

print("Maior que 1000000: ",cities[cities>1000000])

    # ---- more functions:

d = {"Seatle":100,"San Francisco":500,"San Jose":150,"London":1200,"Tokyo":1600}
cities = pd.Series(d)
print('\n')
print(cities)

    # filtering
print("\n---- Cities < 1000: ----\n", cities<1000)

    # replace
cities["San Francisco"]=600
print('\n')
print(cities)

cities[cities<1000]= 750
print('\n')
print(cities)

print('Seatle' in cities)
print('Delfhi' in cities)


print('\n')
print(cities/10)

print(cities.isnull())

