mystring=input("Enter string:")
n1=0
n2=0
n3=0
n4=0
for i in mystring:
	if(i.islower()):
		n1=n1+1
	elif(i.isupper()):
		n2=n2+1
	elif(i.isspace()):
		n3=n3+1
	elif(i.isdigit()):
		n4=n4+1

print("The number of lowercase characters is:")
print(n1)
print("The number of uppercase characters is:")
print(n2)
print("The number of spaces is:")
print(n3)
print("The number of digits is:")
print(n4)