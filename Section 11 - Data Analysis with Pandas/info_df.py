import pandas as pd
local = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/programminglanguage.csv'
program  = pd.read_csv(local, names=["Year","Name","Company","Predecessor"],header = 0)

print(program.head())
print("")
print(program.dtypes)
print("")
print(program.describe)
print("")
print(program.set_index('Year').head())
print("")
print(program.set_index('Year', inplace=True))
print(program) # modified by comand ^^^^True
print("")
print(program.index[[1,12,32]])
print("")
