from catalog import Catalog
"""Hosptial simulator for trackig patients and procedure information

Author:Matt Bobbitt 
Class: CSI-260-01
Assignment: Week 6 library Lab
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

def main():
	menu = """
	Library Menu \n
	1. Search catalog \n
	2. Print the entire catalog\n
	3. Add item to catalog\n
	4. Remove item from catalog\n
	5. Exit\n"""

	lib = Catalog()
	quit_prog = False
	
	while not quit_prog:
		print(menu)
		opt = input("enter an option: ")
		if opt.isnumeric():
			opt = int(opt)
		match opt:
			case 1:
				pass

			case 2:
				lib.__str__()
			
			case 3:
				lib.add()
			
			case 4:
				lib.remove()
			
			case 5:
				lib.save_pickle()
				quit_prog = True
			
			case other:
				print("input valid option [1-5]")		
main()	
