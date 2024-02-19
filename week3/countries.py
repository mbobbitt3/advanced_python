# Author:Matt Bobbitt 
# Class: CSI-270-01
# Certification of Authenticity:
# I certify that this is entirely my own work, except where I have given fully
# documented
# references to the work of others. I understand the definition and consequences
# of
# plagiarism and acknowledge that the assessor of this assignment may, for the
# purpose of
# assessing this assignment reproduce this assignment and provide a copy to another
# member
# of academic staff and / or communicate a copy of this assignment to a plagiarism
# checking
# service(which may then retain a copy of this assignment on its database for the
# purpose
# of future plagiarism checking).

class Country:

	def __init__(self, name, area, population):
		"""init fucntion for name popualtion and area"""
		self.name = name
		self.population = population
		self.area = area

	def get_name(self):
		"""returns name of country"""
		return self.name

	def is_larger(self, country):
		"""takes two country objects and compares area, returning true false based on
		the area if country1 is bigger than country2"""
		if self.area > country.area:
			return True
		else:
			return False
	
	def pop_dens(self):
		"""calculates population density of country to 4 decimal places and returns result"""
		pd = "{:.4f}".format(self.population / self.area)
		print(self.name, "has a population density of:", pd, "people per sq km")
		return pd

	def summary(self):
		"""returns summary of previous methods using print statement"""
		pd = self.pop_dens()
		print("{} has a area of {} sq km, a population of {} people, and a population density of {} people per sq km".format(
			self.name, self.area, self.population, pd))
	def __str__(self):
		"""cleaner way of printing summary"""
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
