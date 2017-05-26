#coding=UTF-8
#调用一个不存在的类的属性时会报错

#__getattr__

class Student(object):
    def __init__(self):
        self.name='chenlong'
        
    #Python还有另一个机制，那就是写一个__getattr__()方法，动态返回一个属性,访问不存在的属性    
    def __getattr__(self,attr):
        if attr=='score':
            return 00
        if attr == 'age': #返回函数
            return lambda:25
        raise AttributeError('Error %s'%(s))
   #注意，只有在没有找到属性的情况下，才调用__getattr__，已有的属性，比如name，不会在__getattr__中查找
        
s=Student()

print s.name        

print s.score

print s.aa
print s.age()


