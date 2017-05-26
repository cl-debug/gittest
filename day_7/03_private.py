#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__，在Python中，实例的变量名如果以__开头，就变成了一个私有变量（private），只有内部可以访问，外部不能访问
class Student(object):
	"""docstring for Student"""
	def __init__(self, name,age):
		self.__name=name
		self.__age=age

	#def print_params():
	#	 print '%s: %s' % (self.__name, self.__age)

	#外部代码要获取name和score
	def get_name(self):
		return self.__name

	def get_age(self):
		return self.__age	

bar =Student("11","22")
print(bar.get_age())

#需要注意的是，在Python中，变量名类似__xxx__的，
#也就是以双下划线开头，并且以双下划线结尾的，是特殊变量，特殊变量是可以直接访问的，不是private变量，所以，不能用__name__、__score__这样的变量名。