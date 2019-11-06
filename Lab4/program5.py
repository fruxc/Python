class Cf:
	def convert(self):
		n = int(input("Enter number of inputs :- \n"))
		a = []
		for i in range(0,n):
			c = float(input("Enter celsius to convert :- \n"))
			a.append(c)
		return a
		
ob = Cf()
t = ob.convert()
f = list(map(lambda x: (float(9)/5)*x + 32, t))
print(f)