import math

print("Format is ax^2+bx+c and should be integer\n")
print("Enter the values of a, b and c \n")

a = int(input('Enter a : '))
b = int(input('Enter b : '))
c = int(input('Enter c : '))

print("Giver Equation : %f x**2 + %f x + %f "%(a,b,c))

u = b**2 - 4*a*c
u = math.sqrt(u)

r1 = (((-b) + u)/(2*a))
r2 = (((-b) - u)/(2*a))

print("There are 2 roots: %f and %f" % (r1, r2))

