import calculator
 
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
 
while True:
	print("Select one of the operations \n1.Addition \n2.Subtract \n3.Multiplication \n4.Division \n5.Mod \n6.Exit")
	select = int(input(" "))
 
	if(select == 1):
        print(calculator.Add(x, y))
    	
	elif(select == 2):
        print(calculator.Sub(x, y))
    	
	elif(select == 3):
        print(calculator.Mul(x, y))
    	
	elif(select == 4):
       print(calculator.Div(x, y))
 
	elif(select == 5):
        print(calculator.Mod(x, y))
    	
	elif(select == 6):
    	break
	else:
        print("Invalid input")
 