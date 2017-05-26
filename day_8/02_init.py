class student(object):

	def __init__(self,name,age):
		self.name=name
		self.age =age

	def print_name(self):
		print(self.name)	

bar = student('11','22')

bar.print_name()