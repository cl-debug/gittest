#coding=UTF-8

#使用__slots__

class Student(object):
    pass

s= Student()

#给实例绑定一个属性
s.name='chenlong'

print s.name

#给实例绑定一个方法
def set_age(self,age):
    
    self.age=age

from types import MethodType

s.set_age = MethodType(set_age,s,Student) # 给实例绑定一个方法

s.set_age(24) # 调用实例方法

print(s.age)    

#但是，给一个实例绑定的方法，对另一个实例是不起作用的
s2=Student()

#为了给所有实例都绑定方法，可以给class绑定方法

def set_sorce(self,sorce):
    self.sorce=sorce
    
Student.set_sorce=MethodType(set_sorce,None,Student)

s.set_sorce(5)    

print s.sorce

s2.set_sorce(99)

print s2.sorce
    
    
    
    
    