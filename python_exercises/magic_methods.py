class Student:
	def __init__(self,name):
		self.name=name

movies = ['123','xyz']
print(movies.__class__)
print("ih".__class__)
print(len(movies))

class Garage:
	def __init__(self):
		self.cars = []
	def __len__(self):
		return len(self.cars)
	def __getitem__(self,i):
		return self.cars[i]



ford = Garage()
ford.cars.append('Volkswagen')
ford.cars.append('BMW')
print(ford)
print(ford[0])
for car in ford:
	print(car)