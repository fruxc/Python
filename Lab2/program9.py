
n = int(input("Enter any number to check if it is palindrome or not :-\n"))

rev = 0
temp = n

while(temp>0):
	rev = rev * 10
	rev = rev + (temp % 10)
	temp = temp // 10

print("Reverse of given input is : - ",rev)

if(rev == n):
	print("Number is palindrome")
else:
	print("Number is not palindrome")
