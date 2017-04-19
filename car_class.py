class Car(object):
	def __init__(self,typ = "saloon", model = 'GM', name = 'General'):
		self.type = typ
		self.model = model
		self.name = name
		
	def car_doors(self):
		if self.name == 'Koenigsegg' or self.name =='Porshe':
			return 2
		else:
			return 4

	def car_wheels(self):
		if self.type == 'trailer':
			return 8
		else:
			return 4
	def is_saloon(self):
		if self.type == "saloon":
			return True
		else:
			return False

	def drive(self,x):
		if x == 3:
			self.speed = 1000
		elif x == 7:
			self.speed = 77
		else:
			self.speed = 56
		return self


