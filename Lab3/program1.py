a = []
c = []
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
	b=int(input("Enter element:"))
	a.append(b)
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
	b=int(input("Enter element:"))
	c.append(b)
s = a+c

n = len(s)
for i in range(n):
	for j in range(0, n-i-1):
		if s[j] > s[j+1] :
			temp = s[j]
			s[j] = s[j+1]
			s[j+1] = temp
for i in range(0,n):
	print("\n \t Element : ",s[i])

print("Sorted :",n)
print("2nd Last element of the list is :",s[n-2])