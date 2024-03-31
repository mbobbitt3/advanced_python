from abc import ABC, abstractmethod

class LibraryItem(ABC):
	"""Base class for all items stored in a library catalog
	Provides a simple LibraryItem with only a few attributes"""
  
	def __init__(self, name, callNumber, tags = None):
		""" Initialize a LibraryItem
		:param name: (string) Name of item
		:param callNumber: (string) Local identifying number for the item
		:param tags: (list) List of CategoryTags
		"""
		super().__init__()
		self.name = name
		self.callNumber = callNumber
		if tags:
			self.tags = tags
		else:
			self.tags = []

	@abstractmethod
	def __str__(self):
		""" Print the information of a LibraryItem
		"""
		print(self.__class__.__name__)
		print("Call Number: ", self.callNumber)
		print("Title: ", self.name)

class Book(LibraryItem):
	"""subclass item for book"""
	def __init__(self, name, callNumber, authors, desc, pub, yr, tags = None):
		"""book tkaes auhtor, description, publisher, and year as init values"""
		super().__init__(name, callNumber, tags)
		self.auth = authors
		self.desc = desc
		self.pub = pub
		self.yr = yr

	def __str__(self):
		"""print book info"""
		super().__str__()
		print("Authors: ", self.auth, "description", self.desc, "publisher: ", self.pub, "year: ", self.yr)


class Dvd(LibraryItem):
	"""subclass of LibItem for DVD"""
	def __init__(self, name, callNumber, directors, desc, producers , yr, tags = None):
		"""DVD tkaes drector , description, producers , and year as init values"""
		super().__init__(name, callNumber, tags)
		self.dir = directors 
		self.desc = desc
		self.prods = producers
		self.yr = yr

	def __str__(self):
		"""print book info"""
		super().__str__()
		print("Director: ", self.dir, "description", self.desc, "Prodcuers: ", self.prods, "year: ", self.yr)

class Magazine(LibraryItem):
	"""subclass of LibItem for magazine"""
	def __init__(self, name, callNumber, desc, pub, yr, tags = None):
		"""book tkaes auhtor, description, publisher, and year as init values"""
		super().__init__(name, callNumber, tags)
		self.desc = desc
		self.pub = pub
		self.yr = yr

	def __str__(self):
		"""print magazine info"""
		super().__str__()
		print("description", self.desc, "publisher: ", self.pub, "year: ", self.yr)


