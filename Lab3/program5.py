class OxfordDictionary(object):
	oxfordDict = {'Nishita': 'a human being','marathon': 'a running race that is about 4 miles','resist': 'to remain strong against the force','run': 'to move with haste; act quickly'}	
	
	def __init__(self):
		print(self.oxfordDict)

	def random(self):
		self.oxfordDict['shoe'] = 'an external covering for the human foot'
		print (" Shoe : ",self.oxfordDict['shoe'])
		
	def added(self):
		k = input("Enter the key\n")
		p = input("Enter the pair\n")
		self.oxfordDict[k] = p
		print(" Added ",k," : ",self.oxfordDict[k])

	def display(self):
		print (self.oxfordDict)
	
	def search(self):
		key = input("Enter Key Value to Search\n")
		if key in self.oxfordDict:
			print("Searched Element is ",key," : ",self.oxfordDict[key])
		else :
			print("Key Not Found");
		
	def delete(self):
		key = input("Enter Key Value to delete\n")
		if key in self.oxfordDict:
			print("Deleting Element ",key," : ",self.oxfordDict[key])
			del self.oxfordDict[key]
		else :
			print("Key Not Found");

obj = OxfordDictionary()

while True:
	print("\n1.To Add \n2.To add static value \n3.To Delete\n4.To Search\n5.To Display\n6.To Quit")
	choice = int(input("Enter choice\n"))
	if choice==1:
		obj.added()
	elif choice==2:
		obj.random()
	elif choice==3:
		obj.delete()
	elif choice==4:
		obj.search()
	elif choice==5:
		obj.display()
	elif choice==6:
		break
	else:
		print("Invalid choice, please choose again.\n")
print("Thank you!!!")