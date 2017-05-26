#Python中，实例的变量名如果以__开头，就变成了一个私有变量（private）

class Student(object):
	def __init__(self,name,age):
		self.__name=name
		self.__age =age

	def print_name(self):
		print(self.__name)

	def set_name(self,new_name):
		self.__name=new_name



bar = Student('11','22')

bar.name='33' #私有的变量外部无法访问

bar.print_name()		

bar.set_name('44')

bar.print_name()

#在Python中，变量名类似__xxx__的，也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量