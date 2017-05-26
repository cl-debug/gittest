#coding=UTF-8

#如果我们想要限制class的属性怎么办？比如，只允许对Student实例添加name和age属性。
#Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性

class Student(object):
    __slots__=('name','age')
    
s=Student()

s.name='chenlong'

s.age='18'    

s.sorce='20'

#使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用


#除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。