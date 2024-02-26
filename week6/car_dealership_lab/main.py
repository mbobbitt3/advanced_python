from vehicle_types import Car, Motorcycle, Truck
from vehicle import Vehicle
class Menu:
	"""display menu and setup menu option"""
	def __init__(self):
		self.vehicles = []
		self.options  = {
			"1":self.show_inventory,
			"2":self.add_car,
			"3":self.add_moto,
			"4":self.add_truck,
			"5":self.quit
		}
	def show_menu(self):
		print("""\
			Menu:

			1. Show all vehicles
			2. Add a car
			3. Add a motocycle
			4. Add a truck 
			5. Quit
			"""
		)
	def inventory_system(self):
		"""inventory system code is here to manage the garage"""
		while True:
			self.show_menu()
			option = input("Enter a option: ")
			act = self.options.get(option)
			if act:
				act()
			else:
				print("[0] is not a valid input".format(choice))

	def show_inventory(self):
		for i in self.vehicles:
			print(i)
			
	def add_car(self):
		self.vehicles.append(
			Car(
				int(input("Enter miles on vehcile: ")),
				input("Enter make of vehicle: "),
				input("Enter Model of vehicle: "),
				int(input("Enter year of vehicle: ")),
				int(input("Enter cost of vehicle: "))
			)
		)

	def add_truck(self):
		self.vehicles.append(
			Truck(
				int(input("Enter miles on vehcile: ")),
				input("Enter make of vehicle: "),
				input("Enter Model of vehicle: "),
				int(input("Enter year of vehicle: ")),
				int(input("Enter cost of vehicle: "))
			)
		)
	def add_moto(self):
		self.vehicles.append(
			Motorcycle(
				int(input("Enter miles on vehcile: ")),
				input("Enter make of vehicle: "),
				input("Enter Model of vehicle: "),
				int(input("Enter year of vehicle: ")),
				int(input("Enter cost of vehicle: "))
			)
		)
	def quit(self):
		"""this exits the program"""
		sys.exit(0)
if __name__ == '__main__':
	Menu().inventory_system()	
