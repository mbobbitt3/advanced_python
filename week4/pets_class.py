class Pet:
	class_info = "pet animals"
	"""	
	This keeps the method bound to the class it si using by using the static method tag
	@staticmethod
	def about():
		print("this class is about", Pet.class_info, "!")
	"""
	#class method allows this to be used across different classes
	@classmethod
	def about(cls):
		print("this class is about", cls.class_info, "!")

class Dog(Pet):
	class_info = "man's best friend"

class Cat(Pet):
	class_info = "thinks they are superior to man"

Pet.about()
Cat.about()
Dog.about()
