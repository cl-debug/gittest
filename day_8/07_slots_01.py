class Student(object):
	pass

#实例绑定一个属性

s= Student()

s.name='chenlong'

print(s.name)

#给实例绑定一个方法

def set_age(self,age):
	self.age=age
		
from types import MethodType

s.set_age=MethodType(set_age,Student)

s.set_age(25)

#s.age		