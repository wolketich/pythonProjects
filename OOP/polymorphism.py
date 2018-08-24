# Polymorphism allows child classes to completely override methods defined in parent class

class Bird:

	def intro(self):
		print("There are many types of birds.")

	def flight(self):
		print("Most of the birds can fly but some cannot.")

class sparrow(Bird):

    # Override
	def flight(self):
		print("Sparrows can fly.")

class ostrich(Bird):

    # Override
	def flight(self):
		print("Ostriches cannot fly.")

# Create objects
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

# Using same methods, but getting different results
obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()
