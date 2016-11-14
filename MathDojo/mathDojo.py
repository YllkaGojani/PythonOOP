class MathDojo(object):
	def __init__(self):
		self.result = 0

	#part 1	
	# def add(self,*adders):
	# 	for adder in adders:
	# 		self.result += adder
	# 	# print self.result
	# 	return self
	# def subtract(self,*subs):
	# 	for sub in subs:
	# 		self.result -= sub
	# 	# print self.result
	# 	return self	

# md = MathDojo().add(2).add(2,5).subtract(3,2).result
# print md

	#part 2
# 	def add(self, *adders):
# 	    for adder in adders:
# 	        if isinstance(adder, list):
# 	            for idx in adder:
# 	                self.result += idx
# 	        else:
# 	            self.result += adder
# 	    return self

# 	def subtract(self, *subs):
# 	    for sub in subs:
# 	        if isinstance(sub, list):
# 	            for idx in sub:
# 	                self.result -= idx
# 	        else:
# 	            self.result -= sub
# 	    return self


# md2 = MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
# print md2

	#part 3
	def add(self, *adders):
	    for adder in adders:
	        if isinstance(adder, (list,tuple)):
	            for idx in range(0,len(adder)):
	                self.result += adder[idx]
	        else:
	            self.result += adder
	    return self

	def subtract(self, *subs):
	    for sub in subs:
	        if isinstance(sub, (list,tuple)):
	            for idx in range(0,len(sub)):
	                self.result -= sub[idx]
	        else:
	            self.result -= sub
	    return self	

md3 = MathDojo().add([3,7,8],(5,7),1).subtract([3, 3], (2, 4),(2,2)).result
print md3	    