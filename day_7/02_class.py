class Student(object):
	def __init__(self, name,age):
		self.__name = name
		self.__age  = age
	def get_name(self):
		return self.__name
	def get_age(self):
		print(self.__age)			

p=Student('11','22')

p.get_age()      
		