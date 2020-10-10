# OOP 
class Employee:
	#Double underscore means private access
	#Without double score its public access and you won't need setters and getters
	__name = None
	__id = 0
	__salary = 0
	#Setters and Getters

	def set_name(self,name):
		self.__name = name

	def get_name(self):
		return self.__name

	#Constructor
	def __init__(self,name,id,salary):
		self.__name = name
		self.__id = id
		self.__salary = salary


Ansh = Employee('Ansh',00,123456)
print(Ansh.get_name())
