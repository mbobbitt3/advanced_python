from abc import ABC, abstractmethod
class Polygon(ABC):
	def talk(self):
		print('i am a polygon')

	@abstractmethod
	def num_sides(self):
		pass #abstract methods are always bodyless

class Triangle(Polygon):
	def __init__(self):
		print('triangle')
	
	def num_sides(self):
		print('I have 3 sides')

class Square(Polygon):
	sides = 4
	def __init__(self):
		print('square')

	def num_sides(self):
		x = Square.sides
		print('i have', x, 'sides')

class Hexagon(Polygon):
	def __init__(self, sides):
		print('hexagon')
		self.sides = sides
	
	def num_sides(self):
		print('i have', self.sides, 'sides')
	
	def talk(self):
		super().talk()
		self.num_sides()

class Duck():
	def num_sides(self):
		print("i have too many sidesas I am a duck")
	
t = Triangle()
t.num_sides()
s = Square()
s.num_sides()
h = Hexagon(6)
h.num_sides()
h.talk()
d = Duck()
d.num_sides()
