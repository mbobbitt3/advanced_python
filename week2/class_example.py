class pet():
	def __init__(self, name):
		self.name = name 
		self.hunger = 4
		self.boredom = 5
	
	def talk(self):
		print("hello I am: ", self.name)				
		print("hello I am hunger level: ", self.hunger)				
		print("hello I am bored level: ", self.boredom)				

dawg = pet('the big dawg')
dawg.talk()
