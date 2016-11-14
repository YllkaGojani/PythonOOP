class Animal(object):
	def __init__(self):
		self.name = ''
		self.health = 100
	def walk(self):
		print 'Walking'
		self.health -= 1
		return self
	def run(self):
		print 'Running'
		self.health -= 5
		return self
	def displayHealth(self):
		print 'Animal: '+ str(self.name) +' Health: ' + str(self.health) + '\n'	
		return self

animal = Animal()
animal.name = 'A'
animal.walk().walk().walk().run().run().displayHealth()
#Animal object has no attribute fly() or pet()
# animal.fly() 
# animal.pet()	