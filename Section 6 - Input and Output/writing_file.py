#f = open(r"C:\Users\Lucas\Desktop\GitHub\Learn-Python-The-Complete-Python-Programming-Course\Section 6 - Input and Output\Testfile.txt")
f = open('Testfile.txt','w')

f.write("I have entered some tet into this file \n lets see if this works")
f.close()

f = open('Testfile.txt','r')
print(f.read())

# output:
#   I have entered some tet into this file 
#   lets see if this works