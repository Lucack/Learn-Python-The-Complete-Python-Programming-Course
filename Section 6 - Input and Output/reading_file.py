f = open(r"C:\Users\Lucas\Desktop\GitHub\Learn-Python-The-Complete-Python-Programming-Course\Section 6 - Input and Output\Testfile.txt")
print(f.read())
print(f.read()) # dont read twices

    # .tell()
print(f.tell()) # return '90' position cursor

    #  .seek(0,0)   return '0' position cursor
position = f.seek(0,0)
print(f.read())

position = f.seek(0,0)
print(f.read(21))
print(help(open))