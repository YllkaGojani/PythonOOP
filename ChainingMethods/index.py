class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: ' + str(self.price) + '.'
		print 'Maximum speed: ' + str(self.max_speed) + '.'
		print 'Total miles: ' + str(self.miles) + '.\n'
		return self
	def ride(self):
		print 'Riding!'
		self.miles += 10
		return self
	def reverse(self):
		if self.miles <= 0:
			print 'Can not reverse!'
		else:
			print 'Reversing!'
			self.miles -= 5	
		return self			

bike1 = Bike(200,'25mph')
bike1.ride().ride().ride().reverse().displayInfo()	

bike2 = Bike(225,'22mph')
bike2.ride().ride().reverse().reverse().displayInfo()

bike3 = Bike(250,'29mph')
bike3.reverse().reverse().reverse().displayInfo()
	