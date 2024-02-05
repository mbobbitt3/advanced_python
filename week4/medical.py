class Procedure:
	id_num = 0
	def __init__(self, name, date, doctor, cost):
		self.name = name
		self.date =  date
		self.doctor = doctor
		self.cost = cost
		#self.__id = id_num + 1
	
	def __str__(self):
		s = "the procedure " + self.name + " will be performed on " + self.date +\
			" by " + self.doctor + " for " + self.cost + " dollars"
		return s
p = Procedure("kidney harvest", "11/22/24", "Dr. Goldberg", "50,000")
string = p.__str__()
print(string)
