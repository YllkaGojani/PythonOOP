class Underscore(object):
	def map(self,lists,lambda1):
		self.lists = lists
		self.lambda1 = lambda1
		for item in range(len(lists)):
			lists[item] = lambda1(lists[item])
		return lists
	def reduce(self,lists,lambda1):
		self.lists = lists
		self.lambda1 = lambda1
		sum = 0
		for item in range(len(lists)):
			sum += lambda1(lists[item])
		return sum
	def find(self,lists,lambda1):
		self.lists = lists
		self.lambda1 = lambda1
		for item in range(len(lists)):
			if self.lambda1(lists[item]):
				return	lists[item]	
	def filter(self,lists,lambda1):
		self.lists = lists
		self.lambda1 = lambda1
		array = []
		for item in range(len(lists)):
			if self.lambda1(lists[item]):
				array.append(item)	
		i = len(array)-1				
		while i >= 0:
			a = array[i]
			lists.pop(a)
			i = i - 1	
		return lists
	def reject(self,lists,lambda1):
		self.lists = lists
		self.lambda1 = lambda1
		array = []
		for item in range(len(lists)):
			if self.lambda1(lists[item]):
				array.append(item)	
		i = len(array)-1				
		while i >= 0:
			a = array[i]
			lists.pop(a)
			i = i - 1	
		return lists										

_ = Underscore()
mapU = _.map([1,2,3,4,5,6],lambda x:x**2)
# print mapU

reduceU = _.reduce([1,2,3,4,5,6],lambda x: x)
# print reduceU

findU = _.find([1,2,3,4,5,6],lambda x: x % 2 == 0)
# print findU	

filterU = _.filter([1,2,3,4,5,6],lambda x: x % 2 != 0)
# print filterU

rejectU = _.reject([1,2,3,4,5,6],lambda x: x % 2 == 0)
print rejectU		