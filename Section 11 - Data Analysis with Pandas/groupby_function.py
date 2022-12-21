import pandas as pd
local = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/programminglanguage.csv'
program  = pd.read_csv(local, header = 0,names=["Year","Name","Company","Predecessor"])
languages = program.groupby('Name')
print(languages)
print()
print(languages.count().head())
print()
print(languages.size().head())
print()
