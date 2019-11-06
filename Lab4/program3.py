Binary_Storage = []
count = 0
def convertB(n,count):
	if(n>0):
		count=count+1
		Binary_Storage.append(n%2)
		convertB(n//2,count)
while True:
	print("\nPress 0 to quit.\n")
	s = int(input("Enter a decimal number to convert it into binary number:\n"))
	if s==0:
		break
	else:
		convertB(s,-1)
		Binary_Storage.reverse()
		print(*Binary_Storage)
		Binary_Storage.clear()
print("Thank you!!!")
