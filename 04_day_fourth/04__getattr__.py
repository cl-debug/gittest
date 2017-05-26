#coding=UTF-8

class Student(object):
    
    def __init__(self):
        self.name='chenlong'
    #只有找到不存在的属性才调用getattr方法
    def __getattr__(self,attr):
        if attr=="aa":
            return '11'
        
        if attr=='cc':
            return lambda:25 #匿名函数
             
         
     
s=Student()


print s.name     

print s.aa

print s.cc()


        
    