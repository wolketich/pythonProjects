# Define the superclass Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")

# Define the subclass Dog, which has a different speak method
class Dog(Animal):

    
    def __init__(self, name):
        super().__init__(name)

    def speak(self):
        print("Woof!")

# Create an instance of the superclass
animal = Animal("Generic animal")
animal.speak()  # Output: "I am an animal"

# Create an instance of the subclass
dog = Dog("Bobik")
dog.speak()  # Output: "Woof!"
print(dog.name)  # Output: "Fido"
