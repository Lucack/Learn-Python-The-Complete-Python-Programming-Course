#ufn = input("Enter your filename: ")
#ufn = ufn + ".txt"

ufn = "Testfile.txt"
file1 = open(ufn, 'r')
file2 = open('copiedfile.txt','w') 
file2.write(file1.read())  # copying file(r) 1 to file2(w)
file2.close()

file2 = open('copiedfile.txt','r')
file2.seek(0,0)
print(file2.read())