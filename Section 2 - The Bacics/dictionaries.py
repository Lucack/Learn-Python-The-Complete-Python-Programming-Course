students = ["Eric" , 14, "Bob", 12, "Tina", 26, "Chris", 15] 
students = {"Eric":14 , "Bob":12, "Tina":26, "Cris":15}
print(students["Bob"]) #return 12

students["Bob"] = 13 #att
print(students)

del students["Bob"]
print(students)
