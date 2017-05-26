#coding=UTF-8

class Student(object):
    
    def __init__(self,name):
        self.name=name
        
    def __str__(self):
        return 'Student %s' %self.name    
        
s=Student('chenlong')


print s    #<__main__.Student object at 0x0000000001DD2A58>


 
   
        