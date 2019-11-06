class Person:
    name = None
    age = 0
    psDict = {}
    def setData(self,pName,pAge):
        self.name = pName
        self.age = pAge

    def show(self):
        print(self.name)
        print(self.age)
        
class Student:
    id = 0
    def setData(self, pId):
        self.id = pId
    def getId(self):
        return self.id
class Storage:
    def store(self):
        self.psDict[self.id] = self.name,self.age
    def display(self):
        print(self.psDict)

class Resident(Person, Student, Storage):
    def getData(self):
        self.id = input("Enter ID of the student:\n")
        self.name = input("Enter name of the person:\n")
        self.age = input("Enter age of the person:\n")
    def setData(self):
        Person.setData(self, self.name, self.age)
        Student.setData(self, self.id)


n = 'Y'
obj = Resident()
while(True):
    if n == 'Y':
        obj.getData()
        obj.setData()
        obj.show()
        print(obj.getId())
        obj.store()
    elif n == 'N':
        break
    n = input("Want to continue?Y/N\n")
    n = n.upper()
obj.display()
print("Bye!!!")
