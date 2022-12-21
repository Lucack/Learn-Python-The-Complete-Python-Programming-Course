import pandas as pd
local = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/test.csv'
df = pd.read_csv(local)
print(df)
#        Date  A  B   C
# 0  20122022  a  1  10
# 1  21122022  b  2  50
# 2  22122022  c  3  45

print("")
df = pd.read_csv(local, names=['Pizza','Cat','Dog','Cheese'], header = 0)
print(df)

#       Pizza Cat  Dog  Cheese
# 0  20122022   a    1      10
# 1  21122022   b    2      50
# 2  22122022   c    3      45

print("")
df = pd.read_csv(local, usecols=[0,2,3])
print(df)

#        Date  B   C
# 0  20122022  1  10
# 1  21122022  2  50
# 2  22122022  3  45