import os
import pickle
"""Hosptial simulator for trackig patients and procedure information

Author:Matt Bobbitt 
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 19, 2024 11:59 PM

Certification of Authenticity:
I certify that this is entirely my own work, except where I have given
fully-documented references to the work of others. I understand the definition
and consequences of plagiarism and acknowledge that the assessor of this
assignment may, for the purpose of assessing this assignment:
- Reproduce this assignment and provide a copy to another member of academic
- staff; and/or Communicate a copy of this assignment to a plagiarism checking
- service (which may then retain a copy of this assignment on its database for
- the purpose of future plagiarism checking)
"""
class Procedure:
	"""keeps track of procedure information"""
	__last_id = 0
	all_procedures = {}
	def __init__(self):
		"""init data for procedure"""
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
		"""generates unique ID for procedure"""
		if value == 0:
			cls.__last_id += 1
		return cls.__last_id

	def __str__(self):
		"""pretty prints procedure details"""
		s = "Procedure:" + self.name + "\n" + "Performed on: " + self.date + "\n" +\
			" by " + self.doctor + "\n" + "for " + str(self.cost) + " dollars"
		return s
#p = Procedure("kidney harvest", "11/22/24", "Dr. Wock", "50,000")

class Patient:
	"""next availible ID is a private class variable. This class holds 
	various methods related to managing patient information"""
	__last_id = 0
	all_patients = {}
	def __init__(self, fn, ln, addr, phone, contact_name, contact_phone ): 
		"""init method to take patient details"""
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
		#ask for procedure details and adds to patient procedure list 
		procedure = Procedure() #fill in details later
		self.procedures.append(procedure)
		
	@classmethod
	def id(cls, value = 1):
		"""generates patient ID as a private class variable """
		if value == 0:
			cls.__last_id += 1
		print(cls.__last_id)
		return cls.__last_id
	
	def __str__(self):
		"""nicely prints patient info"""
		s = self.fn + "\n"
		s += self.ln + "\n"
		s += self.addr + "\n"
		s += self.phone + "\n"
		s += self.contact_name + "\n"
		s += self.cont_phone + "\n"
		for proc in self.procedures:
			s += proc.__str__()
		return s
	@classmethod	
	def get_patient(cls, id_num):
		"""takes patient id and searches for ID in dict then prints patient info"""
		if id_num in Patient.all_patients:
			print("patient found")
			return Patient.all_patients[id_num]
		else:
			print('patient id not found')
			return None
	@classmethod
	def delete_patient(cls, id_num):
		"""takes patient ID and checks for existence of ID and deletes the patient with specified ID"""
		if id_num in Patient.all_patients:
			del Patient.all_patients[id_num]
		else:
			print("id doesn't exist")
			pass
	@classmethod
	def save_patients(cls):
		"""saves the all patient dictionary into a pickle file"""
		with open("patients.pkl", 'wb') as f:
			pickle.dump(Patient.all_patients, f)
			print("patients saved to file")
	@classmethod	
	def load_patients(cls):
		"""open pickle file with patient data and reassign to all_patients in program for alterations before saving"""
		if os.path.isfile("patients.pkl"):
			with open("patients.pkl", 'rb') as f:
				d = pickle.load(f)
				Patient.all_patients = d #loaded dict into d and reassign all_patients to updated dict 'd'
				Patient.__last_id = list(d.keys())[-1]
