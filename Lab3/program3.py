class StringFreq(object):
	def freq(self, str):
		str_list = str.split() 
		unique_words = set(str_list)
		for words in unique_words :
			print('Frequency of ', words , ' : ', str_list.count(words))

obj = StringFreq()
str = input("Enter a string to check word frequency :- \n")
str = str.lower() 
obj.freq(str)