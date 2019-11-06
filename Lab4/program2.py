fibonacci_cache = {}
def fibonacci(n):
	if n in fibonacci_cache:
		return fibonacci_cache[n]
	if n==1:
		value = 1
	elif n==2:
		value = 1
	elif n>2:
		value = fibonacci(n-2)+fibonacci(n-1)
	fibonacci_cache[n] = value
	return value

while True:
	print("\nPress 0 to quit.\n")
	n = int(input("Enter range for fibonacci series:\n"))
	if n==0:
		break
	else:
		for i in range(1,n+1):
			print("\t fibonacci of ",i," = ",fibonacci(i))

print("Thank you!!!")
