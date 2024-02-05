class Country:

	def __init__(self, name, area, population):
		self.name = name
		self.population = population
		self.area = area

	def get_name(self):
		return self.name

	def is_larger(self, country):
		if self.area > country.area:
			return True
		else:
			return False
	
	def pop_dens(self):
		pd = "{:.4f}".format(self.population / self.area)
		print(self.name, "has a population density of:", pd, "people per sq km")
		return pd

	def summary(self):
		pd = self.pop_dens()
		print("{} has a area of \ 
			{} sq km,and a population density of \
			{pd} people per sq km".format(self.area, self.))
	def __str__(self):
		s =  self.name + " has a population of " + str(self.population) +\
		" people and is " + str(self.area) + "sq km with a pop density of" +\
		str(pd) + " people per sq km"
		return s
can = Country("canada",3487779, 79999999)
usa = Country("usa",6721779, 89867484)
can.get_name()
can.pop_dens()
if can.is_larger(usa):
	print(can.get_name(), "is larger")
else:
	print(usa.get_name(), "is larger")
can.summary()
