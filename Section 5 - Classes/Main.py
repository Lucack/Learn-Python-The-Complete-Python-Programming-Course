class Main:
    pass

from Students import Students

stu1 = Students("Bob",12)

print(stu1)
print(stu1._name)
print(stu1._age)

stu1.displayStudent()

stu2 = Students("Fred",14)


    # function hasattr()
# print( help(hasattr))
print(hasattr(stu1, "_age"))
print(hasattr(stu1, "grade"))

    # function setattr()
print(setattr(stu1, "age", "12"))

# function getattr()
print(getattr(stu1,"age")) 
print(stu1._age)        #or



