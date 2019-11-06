print("Out of 100")

maths = float(input("Marks in Maths?\n"))
science = float(input("Marks in Science?\n"))
english = float(input("Marks in English?\n"))
computer = float(input("Marks in Computer?\n"))
history = float(input("Marks in History?\n"))

if maths<=100 and science<=100 and english<=100 and computer<=100 and history<=100:
	s = "pass"
	sum = maths+science+english+computer+history
	total = 500.00
	p = (sum/total) * 100
	if maths<30 or science<30 or english<30 or computer<30 or history<30:
		s = "fail"
		print("Student is failed in at least one subject")
	elif s != "fail":
		if p>=80:
			print("Grade 'O'")
		elif p>=70:
			print("Grade 'A'")
		elif p>=60:
			print("Grade 'B'")
		elif p>=50:
			print("Grade 'C'")
		elif p>=30:
			print("Grade 'D'")
		elif p<30:
			print("'Fail'")
	print("Percentage = ",p)
else:
	print("Subject Marks are greater than 100, Program Closed!")
