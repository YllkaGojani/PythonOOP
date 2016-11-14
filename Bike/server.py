class Bike(object):
	def __init__(self,price,max_speed):
		self.price = price
		self.max_speed = max_speed
		self.miles = 0
	def displayInfo(self):
		print 'Price: ' + str(self.price) + '.'
		print 'Maximum speed: ' + str(self.max_speed) + '.'
		print 'Total miles: ' + str(self.miles) + '.\n'
	def ride(self):
		print 'Riding!'
		self.miles += 10
	def reverse(self):
		if self.miles <= 0:
			print 'Can not reverse!'
		else:
			print 'Reversing!'
			self.miles -= 5			

bike1 = Bike(200,'25mph')
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()	

bike2 = Bike(225,'22mph')
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

bike3 = Bike(250,'29mph')
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()		