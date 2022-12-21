import pandas as pd
local = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/test.csv'
newcsv = pd.read_csv(local, names=['Food','Price','Quantity'], header = 0, usecols=[1,2,3])
print(newcsv)

newlocal = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/test2.csv'
    
    #.to_csv
newcsv.to_csv(newlocal)
newcsv=pd.read_csv(newlocal)
print(newcsv)
