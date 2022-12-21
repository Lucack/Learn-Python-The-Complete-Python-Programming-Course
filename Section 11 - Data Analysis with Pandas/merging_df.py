import pandas as pd
f1 = pd.DataFrame({'key':range(5),'frame1':['a','b','c','d','e']})
f2 = pd.DataFrame({'key':range(2,7),'frame2':['f','g','h','i','j']})
print()
print(f1)
print()
print(f2)
print()
f3 = pd.merge(f1,f2, on='key')
print(f3)
print()
f3 = pd.merge(f1,f2, on='key', how='right') # f2 is full
print(f3)
print()
f3 = pd.merge(f1,f2, on='key', how='left') # f1 is full
print(f3)
print()
f3 = pd.merge(f1,f2, on='key', how='outer') # everything is full
print(f3)
print()
f3 = pd.merge(f1,f2, on='key', how='inner') # 
print(f3)
print()
f3 = pd.concat([f1,f2]) # 
print(f3)
print()
f3 = pd.concat([f1,f2], axis=1) # better
print(f3)
print()