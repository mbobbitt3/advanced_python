class FunException(Exception):
	def __init__(self):
		print("I am not a clean speaker")
	
	def message(self):
		print("PLEASE BE NICE")
	
	def teach_manners(self):
		print("educated people don't swear")

utter=input("input one word ")
while utter != "nice":
	try:
		raise FunException
	
 	except FunException as e:
		print("That was not nice")
		e.message()
		e.teach_manners()
	
	finally:
		print("go and get ice cream")
	utter=input("input one word ")
print("thank you")

