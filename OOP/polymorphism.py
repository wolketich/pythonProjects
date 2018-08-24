# Define a parent class called Animal
class Animal:
	def __init__(self, name):
		self.name = name

	def speak(self):
		raise NotImplementedError("Subclass must implement abstract method")

# Define two child classes that inherit from Animal
class Dog(Animal):
	def speak(self):
		return "Woof!"

class Cat(Animal):
	def speak(self):
		return "Meow!"

# Define a function that takes an Animal object and calls its speak method
def animal_speak(animal):
	print(animal.speak())

# Create instances of the Dog and Cat classes
my_dog = Dog("Bobik")
my_cat = Cat("Rijik")

# Call the animal_speak function with the Dog and Cat instances
animal_speak(my_dog) # Output: "Woof!"
animal_speak(my_cat) # Output: "Meow!"
