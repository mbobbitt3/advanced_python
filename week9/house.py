

class House:
	def __init__(self, price, color):
		self._price = price
		self._color = color

	@property
	def price(self):
		return self._price

	@price.setter
	def price(self, val):
		if val > 0:
			self._price = val
	
	@price.deleter
	def price(self):
		del self._price

	@property
	def color(self):
		return self._color

	@color.setter
	def color(self, val):
		self._color = val
	
	@color.deleter
	def color(self):
		del self._color

house = House(100000, "red")
print(house.price)
house.price = 120000
print(house.price)
del house.price
print(house.color)
house.color = "blue" 
print(house.color)
del house.color
