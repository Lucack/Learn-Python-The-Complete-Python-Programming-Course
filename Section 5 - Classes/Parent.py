class Parent:
    counter = 10
    def __init__(self):
        print("Class initialized")
    def parentFunc(self):
        print("parentFunc being called")
    def setCounter(self, num):
        Parent.counter = num
    def showCounter(self):
        print(Parent.counter)

class Child(Parent):  # Inheritance
    def __init__(self):
        print("Child class being initialized")
    def childFunc(self):
        print("childFunc being called")
    
c = Child()
c.childFunc()

c.parentFunc()
c.setCounter(20)
c.showCounter()