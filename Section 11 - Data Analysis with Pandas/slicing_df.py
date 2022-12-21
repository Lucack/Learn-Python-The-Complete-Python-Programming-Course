import pandas as pd
local = 'C:/Users/Lucas/Desktop/GitHub/Learn-Python-The-Complete-Python-Programming-Course/Section 11 - Data Analysis with Pandas/programminglanguage.csv'
program  = pd.read_csv(local, names=["Year","Name","Company","Predecessor"],header = 0)
print(program.head(4))
print("")
print(program.tail(1))
print("")
print(program[10:15])
print("")
print(program[300:])
print("")
print('Python' in program['Name'])
print("")

    # Data manipulation: 

print(program['Name'].head(10))
print("")

collums_i_want = ["Name","Predecessor"]
print(program[collums_i_want].head)
print("")

print(program[program.Year>2020])
print("")

print(program[(program.Year>2020) & (program.Company == "Google")]) # and operator
print("")

print(program[(program.Year>2020) | (program.Name == "Python")]) # or operator
print("")

