#coding=UTF-8 
#python 3.0
#枚举类型 为这样的枚举类型定义一个class类型，然后，每个常量都是class的一个唯一实例
#from enum import Enum
#Month= Enum('Month',('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
#for name,member in Month.__merbers__.items():
#   print(name,'=>',member,',',member.value)

class Student(object):    
    def __init__(self,name):
        self.name=name
    
    def __call__(self):
        print ('name %s'%self.name)
        
        
s=Student('name')
s()           

#通过callable()函数，我们就可以判断一个对象是否是“可调用”对象。