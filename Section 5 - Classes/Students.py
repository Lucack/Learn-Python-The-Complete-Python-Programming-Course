class Students:
    def __init__(self,name,age):
        self._name = name
        self._age = age
        
    def displayStudent(self):
        a = print("Students name is", self._name, "and age is", str(self._age))
        return a