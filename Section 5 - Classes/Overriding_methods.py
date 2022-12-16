class Parent:
    def func(self):  #same name function
        print("This is a parent function")
class Child(Parent):
    def func(self): #same name function
        print("This is a child function")
    
c = Child()
c.func() # retunr called function of this class Child()

