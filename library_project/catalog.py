from library import LibraryItem, Book, Dvd, Magazine
import pickle
class Catalog:
	name = "library"
	__items__ = []

	def __init__(self):
		"""init catalog"""
		self.ld_pickle()
		print(self.name, 'created')

	def __str__(self):
		"""prints item"""
		for i in range(len(Catalog.__items__)):
			print("i = ", i, '\n')
			Catalog.__items__[i].__str__()
			print("\n")

	def save_pickle(self):
		with open("catalog.pickle", 'wb') as f:
			pickle.dump(Catalog.__items__, f)

	def ld_pickle(self):
		"""load data from picle file if it cant find the file create with empty lsit"""
		try:
			with open("catalog.pickle", 'rb') as f:
				d = pickle.load(f)
		except IOError:
			with open("catalog.pickle", 'wb') as f:
				d = []
				pickle.dump(d, f)
		Catalog.__items__ = d
	
	def add(self):
		"""adds item to catalog"""	
		i = None 
		cond = False
		while not cond:
			lib_type = input("what item do you want to add: 1 book, 2 dvd, 3 Magazine")
			
			if lib_type.isnumeric():
				lib_type = int(lib_type)
			
			match lib_type:
				case 1:
					i = self.book_add()
					cond = True
				
				case 2:
					i = self.dvd_add()
					cond = True

				case 3:
					i = self.mag_add()
					cond = True
				
				case other:
					print("\n input calid number 1-5")

			if i is not None:
				Catalog.__items__.append(i)


	def remove(self):
		"""remove an item from catlog"""
		s = len(Catalog.__items__)

		if s > 0:
			found = False
			idx = 0
	
		self.__str__()
	
		while not found:
			idx = input('enter an Item number')
			
			if idx.isnumeric():
				idx = int(idx)
			
			else:
				print("input valid number in range 0-", s)
			
			if idx < 0 or idx > s:
				print("input valid number in range 0-", s)

			else:
				found = True
			
			if idx > 0:
				Catalog.__items__.pop(idx - 1)

			else:
				print('item not found')

	def book_add(self):
		""" Creates a Book and adds to the Catalog"""

		return Book(
			input("Name: "),
			int(input("Call Number: ")),
			input("Author(s): "),
			input("Description: "),
			input("Publisher: "),
			int(input("Year Published: "))
		)

	def dvd_add(self):
		""" Creates a Dvd and adds	to the Catalog"""

		return Dvd(
			input("Name: "),
			int(input("Call Number: ")),
			input("direcotrs: "),
			input("Description: "),
			input("Producer: "),
			int(input("Year: "))
		)

	def mag_add(self):
		""" Magazine and adds to the Catalog"""

		return Magazine(
			input("Name: "),
			int(input("Call Number: ")),
			input("Description: "),
			input("Publisher: "),
			int(input("Year: "))
		)
