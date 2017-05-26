class Student(object):
	"""docstring for Student"""
	def get_score(self):
		return self.__sorce

	def set_sorce(self,value):
		if not isinstance(value,int):
			raise ValueError("sorce must be integer")
		if value<0 or value>100:
			raise ValueError("sorce must between 0 and 100")
		self.__sorce=value		
		
s= Student()
s.set_sorce(300)
s.get_score()






class student(object):
	"""docstring for student"""
	def __init__(self, arg):
		super(student, self).__init__()
		self.arg = arg
		