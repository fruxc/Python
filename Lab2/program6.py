import numpy as np

x = int(input("Enter number of rows\n"))
y = int(input("Enter number of columns\n"))

A = np.zeros( (x, y) )

B = np.zeros( (x, y) )

print("Enter elements for matrix A")

for i in range (len(A)):
	for j in range (len(A[0])):
		A[i][j] = input('Enter Element {} x {} = '.format(i+1, j+1))

print("Enter elements for matrix B")

for i in range (len(B)):
	for j in range (len(B[0])):
		B[i][j] = input('Enter Element {} x {} = '.format(i+1, j+1))

C = A + B

print(A)

print("+")

print(B)

print("=")

print(C)