from vehicle_types import Car, Motorcycle, Truck
from vehicle import Vehicle
import sys
"""
menu internface for adding vehicle to car dealership
Author:Matt Bobbitt
Class: CSI-260-01
Assignment: Week 4 Lab
Due Date: February 26, 2024 11:59 PM

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
		"""this method prints the menu"""
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
		"""prints inventory list"""
		for i in self.vehicles:
			print(i)
			
	def add_car(self):
		"""this method is used to add cars to vehicles inventory"""
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
		"""this method is used to add trucks to vehicles inventory"""
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
		"""this method is used to add motorcycles to vehicles inventory"""
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
