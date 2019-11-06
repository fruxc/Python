import math
pi = math.pi
class Circle:
        r = 0
        a = 0
        c = 0
        def __init__(self):
                self.r = 0
                self.a = 0
                self.p = 0

        def getdata(self):
                self.r = float(input("Enter radius of the circle :\n"))

        def area(self):
                self.a = pi*pow(self.r,2)
                print("\n Area of Circle = ",self.a)
                
        def circumference(self):
                self.c = 2*pi*self.r
                print("\n Circumference of Circle = ",self.c)
                      
obj = Circle()
while True:
        print("\n1.Get Data. \n2.Area. \n3.Circumference. \n4.To Quit.\n")
        choice = int(input("Enter choice :-\n"))

        if choice==1:
                obj.getdata()
        elif choice==2:
                obj.area()
        elif choice==3:
                obj.circumference();
        elif choice==4:
                break
        else:
                print("Invalid choice, please choose again.\n")
print("Thank you!!!")
