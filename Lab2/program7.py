print("Months : \n1)January\n2)February\n3)March\n4)April\n5)May\n6)June\n7)July\n8)August\n9)September\n10)October\n11)November\n12)December")

s = input("Enter any month to know number of days \n")

if s == "February":
	print("Number of days = 28/29")

elif s == "January" or s == "January" or s == "March" or s == "May" or s == "July" or s == "August" or s == "October" or s == "December":
	print("Number of days = 31")
elif s == "April" or s == "June" or s == "September" or s == "November":
	print("Number of days = 30")
else :
	print("Invalid Month")
