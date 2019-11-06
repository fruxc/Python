global all_students
global n
class StudentDictionary(object):
        all_students = {}
        n = 0
        def __init__(self, x):
                for i in range(0,x):
                        self.all_students[i] = {}
                self.n=x
                for i in range(0,x):
                        self.all_students[i]['Name']=input('Enter the name of student: ')
                        print (self.all_students[i]['Name'])
                        self.all_students[i]['RollNo']=input('Enter the roll number of student: ')
                        print (self.all_students[i]['RollNo'])
                        self.all_students[i]['Address']=input('Enter the address of student: ')
                        print (self.all_students[i]['Address'])
                        self.all_students[i]['Age']=input('Enter the age of student: ')
                        print (self.all_students[i]['Age'])
                        self.all_students[i]['Class']=input('Enter the class of student: ')
                        print (self.all_students[i]['Class'])
                        self.all_students[i]['Mark1']=int(input('Enter the marks in subject 1: '))
                        print (self.all_students[i]['Mark1'])
                        self.all_students[i]['Mark2']=int(input('Enter the marks in subject 2: '))
                        print (self.all_students[i]['Mark2'])
                        self.all_students[i]['Mark3']=int(input('Enter the marks in subject 3: '))
                        print (self.all_students[i]['Mark3'])
                        self.all_students[i]['Mark4']=int(input('Enter the marks in subject 4: '))
                        print (self.all_students[i]['Mark4'])
                        self.all_students[i]['Mark5']=int(input('Enter the marks in subject 5: '))
                        print (self.all_students[i]['Mark5'])
                        self.all_students[i]['Total'] = self.all_students[i]['Mark1'] + self.all_students[i]['Mark2'] + self.all_students[i]['Mark3'] + self.all_students[i]['Mark4'] + self.all_students[i]['Mark5']
                        print("Total is: ", self.all_students[i]['Total'])
                        self.all_students[i]['Average'] = self.all_students[i]['Total']//5
                        print ("Average is :", self.all_students[i]['Average'])
                print(self.all_students)

        def added(self):
            self.n = self.n+1
            i = self.n-1
            self.all_students[i] = {}
            self.all_students[i]['Name']=input('Enter the name of student: ')
            print (self.all_students[i]['Name'])
            self.all_students[i]['RollNo']=input('Enter the roll number of student: ')
            print (self.all_students[i]['RollNo'])
            self.all_students[i]['Address']=input('Enter the address of student: ')
            print (self.all_students[i]['Address'])
            self.all_students[i]['Age']=input('Enter the age of student: ')
            print (self.all_students[i]['Age'])
            self.all_students[i]['Class']=input('Enter the class of student: ')
            print (self.all_students[i]['Class'])
            self.all_students[i]['Mark1']=int(input('Enter the marks in subject 1: '))
            print (self.all_students[i]['Mark1'])
            self.all_students[i]['Mark2']=int(input('Enter the marks in subject 2: '))
            print (self.all_students[i]['Mark2'])
            self.all_students[i]['Mark3']=int(input('Enter the marks in subject 3: '))
            print (self.all_students[i]['Mark3'])
            self.all_students[i]['Mark4']=int(input('Enter the marks in subject 4: '))
            print (self.all_students[i]['Mark4'])
            self.all_students[i]['Mark5']=int(input('Enter the marks in subject 5: '))
            print (self.all_students[i]['Mark5'])
            self.all_students[i]['Total'] = self.all_students[i]['Mark1'] + self.all_students[i]['Mark2'] + self.all_students[i]['Mark3'] + self.all_students[i]['Mark4'] + self.all_students[i]['Mark5']
            print("Total is: ", self.all_students[i]['Total'])
            self.all_students[i]['Average'] = self.all_students[i]['Total']//5
            print ("Average is :", self.all_students[i]['Average'])

        def display(self):
                print (self.all_students)

        def search(self):
                key = input("Enter Key Value to Search\n")
                for key in self.all_students:
                        if key in self.all_students:
                                print("Searched Element is ",key," : ",self.all_students[key])
                        else :
                                print("Key Not Found");

        def delete(self):
                key = input("Enter Key Value to Delete\n")
                for key in self.all_students:
                        if key in self.all_students:
                                print("Deleting Element ",key," : ",self.all_students[key])
                                del self.all_students[key]
                                break
                        else :
                                print("Key Not Found")
            
        def update(self):
                key = input("Enter Key Value to Update\n")
                i = key
                for i in self.all_students:
                        if i in self.all_students:
                                self.all_students[i]['Name']=input('Enter the name of student: ')
                                print (self.all_students[i]['Name'])
                                self.all_students[i]['RollNo']=input('Enter the roll number of student: ')
                                print (self.all_students[i]['RollNo'])
                                self.all_students[i]['Address']=input('Enter the address of student: ')
                                print (self.all_students[i]['Address'])
                                self.all_students[i]['Age']=input('Enter the age of student: ')
                                print (self.all_students[i]['Age'])
                                self.all_students[i]['Class']=input('Enter the class of student: ')
                                print (self.all_students[i]['Class'])
                                self.all_students[i]['Mark1']=int(input('Enter the marks in subject 1: '))
                                print (self.all_students[i]['Mark1'])
                                self.all_students[i]['Mark2']=int(input('Enter the marks in subject 2: '))
                                print (self.all_students[i]['Mark2'])
                                self.all_students[i]['Mark3']=int(input('Enter the marks in subject 3: '))
                                print (self.all_students[i]['Mark3'])
                                self.all_students[i]['Mark4']=int(input('Enter the marks in subject 4: '))
                                print (self.all_students[i]['Mark4'])
                                self.all_students[i]['Mark5']=int(input('Enter the marks in subject 5: '))
                                print (self.all_students[i]['Mark5'])
                                self.all_students[i]['Total'] = self.all_students[i]['Mark1'] + self.all_students[i]['Mark2'] + self.all_students[i]['Mark3'] + self.all_students[i]['Mark4'] + self.all_students[i]['Mark5']
                                print("Total is: ", self.all_students[i]['Total'])
                                self.all_students[i]['Average'] = self.all_students[i]['Total']//5
                                print ("Average is :", self.all_students[i]['Average'])
                                break
                        else :
                                print("Key Not Found");
    

n = int(input("Please enter number of students:"))
obj = StudentDictionary(n)
while True:
    print("\n1.To Add. \n2.To Update. \n3.To Delete. \n4.To Search. \n5.To Display. \n6.To Quit.")
    choice = int(input("Enter choice :-\n"))
    if choice==1:
        obj.added()
    elif choice==2:
        obj.update()
    elif choice==3:
        obj.delete()
    elif choice==4:
        obj.search()
    elif choice==5:
        obj.display()
    elif choice==6:
        break
    else:
        print("Invalid choice, please choose again.\n")
print("Thank you!!!")









