class Procedure:
	__last_id = 0
	all_procedures = {}
	def __init__(self):
		name = input("what is the patient name: ")
		date = input("Enter date of procedure: ")
		doctor = input("Doctor of procedure: ")
		cost = float(input("Cost of procedure (USD): "))
		self.name = name
		self.date =  date
		self.doctor = doctor
		self.cost = cost
		self.id = Procedure.id(0)
		Procedure.all_procedures[self.id] = self

	@classmethod
	def id(cls, value = 1):
		if value == 0:
			cls.__last_id += 1
		return cls.__last_id

	def __str__(self):
		s = "Procedure:" + self.name + "\n" + "Performed on: " + self.date + "\n" +\
			" by " + self.doctor + "\n" + "for " + str(self.cost) + " dollars"
		return s
#p = Procedure("kidney harvest", "11/22/24", "Dr. Goldberg", "50,000")

class Patient:
	"""next availible ID is a private class variable. This class holds 
	various methods related to managing patient information"""
	__last_id = 0
	all_patients = {}
	def __init__(self, fn, ln, addr, phone, contact_name, contact_phone ): 
		"""init class to take patient details"""
		self.fn = fn
		self.ln = ln
		self.addr = addr
		self.phone = phone
		self.contact_name = contact_name
		self.cont_phone =  contact_phone	
		self.id = Patient.id(0)
		Patient.all_patients[self.id] = self
		self.procedures = [] #list of medical.procedure objects

	def add_procedure(self):
		#ask for procedure details 
		procedure = Procedure() #fill in details later
		self.procedures.append(procedure)
		
	@classmethod
	def id(cls, value = 1):
		if value == 0:
			cls.__last_id += 1
		return cls.__last_id
	
	def __str__(self):
		s = self.fn + "\n"
		s += self.ln + "\n"
		s += self.addr + "\n"
		s += self.phone + "\n"
		s += self.contact_name + "\n"
		s += self.cont_phone + "\n"
		for proc in self.procedures:
			s += proc.__str__()
		return s
p1 = Patient("nott", "notyt", "12321", "1232", "wiqe", "120293")
p2 = Patient("jones", "jameson", "12321", "1232", "wiqe", "120293")
p1.add_procedure()
print(p1)
