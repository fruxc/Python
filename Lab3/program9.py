def Count(f):
	count = 0
	for i in f:
		if isinstance(i, tuple):
			break
		count = count + 1
	return count

MyList = [4, 5, 6, 10, 11, 2, 4, (7, 8, 9)]
print(Count(MyList))