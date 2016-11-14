class Car(object):
	def __init__(self,price,speed,fuel,mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (self.price > 10000):
			self.tax = 0.15
		else:
			self.tax = 0.12
	def display_all(self):
		print 'Price: ' + str(self.price)
		print 'Speed: ' + str(self.speed)
		print 'Fuel: ' + str(self.fuel)
		print 'Mileage: ' + str(self.mileage)
		print 'Tax: ' + str(self.tax) + '\n'

c1 = Car(2000,'35mph','Full','15mpg')
c1.display_all()
c2 = Car(2000,'5mph','Not full','105mpg')
c2.display_all()
c3 = Car(2000,'15mph','Kind of full','95mpg')
c3.display_all()
c4 = Car(2000,'25mph','Full','25mpg')
c4.display_all()
c5 = Car(2000,'45mph','Empty','25mpg')
c5.display_all()
c6 = Car(20000000,'35mph','Empty','15mpg')
c6.display_all()					