number = float(input("\nEnter number to check whether it is odd or even :-\n"))

if number == 0:
	print("\nNumber is Zero!!!")
elif number % 2 == 0:
	print("\nNumber is Even!!!")
elif number % 2 == 1:
	print("\nNumber is Odd!!!")
else:
	print("\nInvalid Number!!!")