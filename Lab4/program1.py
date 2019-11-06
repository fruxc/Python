def isPalindrome(string):
	if len(string)<=1:
		return True
	else:
		return string[0]==string[-1] and isPalindrome(string[1:-1])

while True:
	print("\nPress 9 to quit.\n")
	s = input("Enter a string to check if it's Palindrome or not\n");
	s = s.lower();
	if s=="9":
		break
	elif(isPalindrome(s) == True):
		print("String is Palindrome.\n");
	else:
		print("String is not Palindrome.\n");

print("Thank you!!!")
