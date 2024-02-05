class Shapes:
	__counter = 0
	def __init__(self):
		type(self).__counter += 1
		print("shape created")
	
	@classmethod
	def shape_instances():
		return cls, Shapes.__counter

print(Shapes.shape_instances())
square = Shapes()
print(square.shape_instances())
triangle = Shapes()
print(square.shape_instances())

