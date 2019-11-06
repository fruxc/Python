import math

a = int(input('Enter First number : '))
b = int(input('Enter Second number : '))
c = int(input('Enter Third number : '))

p = a+b+c
p = p/2

temp = p*(p-a)*(p-b)*(p-c)

area = math.sqrt(temp)


print("\n Area of Trinangle = ",area)