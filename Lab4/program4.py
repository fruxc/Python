from functools import reduce
class AnonDemo:
	def lambdaDemo(self):
		sum = lambda x, y : x + y
		a=[2,3,5,6,7]
		b=[6,9,2,1,8]
		print(sum(a,b))
		print("Sum of elements using lambda function :- ",sum(3,5))
	def mapDemo(self):
		items=[1,2,3,4,5]
		squared = list(map(lambda x : x**2, items))
		print("Squared Items using map function :- ",squared)
	def filterDemo(self):
		number_list = range(-10, 10)
		less_than_zero = list(filter(lambda x: x < 0, number_list))
		print("Less than zero elements using filter function :- ",less_than_zero)
	def reduceDemo(self):
		product = reduce((lambda x, y: x * y), [1, 2, 3, 4])
		print("Product of all items using reduce function :- ",product)

ob = AnonDemo()
ob.lambdaDemo()
ob.mapDemo()
ob.filterDemo()
ob.reduceDemo()