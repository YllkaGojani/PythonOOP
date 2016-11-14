from animal import Animal
class Dog(Animal):
	def __init__(self):
		super(Dog,self).__init__()
		self.health = 150
	def pet(self):
		print 'Pet!'
		self.health += 5
		return self
class Dragon(Animal):
	def __init__(self):
		super(Dragon,self).__init__()
		self.health = 170
	def fly(self):
		print 'Flying!'
		self.health -= 10
		return self	
	def displayHealth(self):
		print 'This is a dragon!'
		super(Dragon,self).displayHealth()
		return self					
			
dog1 = Dog()
dog1.name = 'Max'
dog1.walk().walk().walk().run().run().pet().displayHealth()	

dragon1 = Dragon()
dragon1.name = 'Drakaris'
dragon1.walk().walk().walk().run().run().fly().fly().displayHealth()
	