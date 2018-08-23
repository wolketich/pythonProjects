# Parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("ID Number: {}".format(self.idnumber))
	
# Child class, same as father class, plus a new method and 2 new field.
class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)
		
	def details(self):
		print("My name is {}".format(self.name))
		print("IdNumber: {}".format(self.idnumber))
		print("Post: {}".format(self.post))

# Create a parent object

Vlad = Person('Vladislav', 123456)

# Create a child object
Andrei = Employee(name='Andrei', idnumber=654321, salary=35000, post='Senior Developer')

# Vlad has only 2 methods, display and details (Parent class)
Vlad.display()
Vlad.details()

# Andrei has same methods as Vlad, but method Details is updated to support more fields.
Andrei.display()
Andrei.details()