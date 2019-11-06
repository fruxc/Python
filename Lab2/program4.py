n = int(input(" Enter any number to check "))

sum = 0

temp = n
count = 0

while(temp>0):
	temp //= 10
	count = count + 1

temp = n

while(temp>0):
	t = temp%10
	sum += t**count
	temp //= 10

if n==sum :
	print("%d Armstrong Number"%n)
else:
	print(n,"is not an Armstrong number")