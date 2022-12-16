f = open('Testfile.txt','a') # mode: 'a'
f.write("\n This is my appending text to my Testfile")
f.close()

f = open('Testfile.txt','r') # mode: 'r'
print(f.read())

# output:
#   I have entered some tet into this file 
#   lets see if this works
#   This is my appending text to my Testfile

f.close()

f = open('Testfile.txt','a+') # mode: 'a+'
f.write("\n This is something")
f.seek(0,0)
print(f.read())


