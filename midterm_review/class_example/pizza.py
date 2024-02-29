import math
#protected varibales can onyl be accessed via methods in the class
class Pizza:
	pizzas_made = 0
	
	def __init__(self, diameter, ingredients):
		self.radius = diameter/2
		self.ingredinets = ingredients
		self.__allergen = "wheat"
		self.__class__.pizzas_made += 1

	def __repr__(self):
		return(f"Pizza({self.radius !r}", f"{self.ingredients}")
	
	
	def area(self):
		return self.circle_area(self.radius)

	def allergens(self):
		return self.__allergens

	@staticmethod
	def circle_area(r):
		return r ** 2 * math.pi

	@classmethod
	def margarita(cls):
		print("making a margharita")
		return cls(16, ["mozz", "tomatoes"])
	
	@classmethod
	def hawaiian(cls):
		print("making a hawaiian")
		return cls(16, ["mozz", "tomatoes", "ham", "pineapple"])

	@classmethod
	def made(cls):
		return cls.pizzas_made

class Any(Pizza):
	def __init__(self, diameter, ingredients):
		super().__init__(diameter, ingredients)
		self.add_ing()
		self.remove_ing()

	def remove_ing(self):
		remove = True
		while remove:
			choice = input("Would you like to remove a ingredient?: ").lower()
			if choice != "y":
				ing = input("enter a ingredient: ")
				self.ingredients.remove(ing)
			else:
				remove = False			
	def add_ing(self):
		remove = True
		while remove:
			choice = input("Would you like to a ingredient?: ").lower()
			if choice != "y":
				ing = input("enter a ingredient: ")
				self.ingredients.remove(ing)
			else:
				remove = False

class Pizza_shop:
	total_pizzas = [] 
	def __init__(self, name):
		self.name = name
	
	def menu(self):
		print("1. margherita")
		print("2. Hawaiian")
		print("3. Other options")
		print("4. Close Shift")
		choice = int(input("What Pizza do you want"))
		return choice
	
	def shift(self):
		closed = False 
		while not closed:
			choice = self.menu()
			if choice == 1:
				x= Pizza.margarita()
				self.__class__.total_pizzas.append(x)
			elif choice == 2
				x = Pizza.hawaiian()
				self.__class__.total_pizzas.append(x)
			elif choice == 3:
				start = input("what kind of pizza do you want: ")
				size = int(input("What diameter do you want?: "))
				x = Any(size, start)
				self.__class__.total_pizzas.append(x)
			else:
				closed = True

pizza_place = Pizza_shop("the pizzza joint")
pizza_place.shift()
print(pizza_place.total_pizzas


