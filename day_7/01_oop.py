class student(object):

	def __init__(self,name,age):
		self.name=name
		self.age=age

	def print_self(self):
		print(self.name,'+',self.age)
a= student('1',18)

a.print_self()		



#def print_(age,name):
#	print '%s: %s' % (name,score)

#print_(11,22)	