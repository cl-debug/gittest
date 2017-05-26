#coding=UTF-8

class Student(object):
    
    def get_sorce(self):
        return self.sorce
    
    def set_sorce(self,value):
        if not isinstance(value, int):
            raise ValueError('sorce must be an intger')
        
        if value >100 or value<0:
            raise ValueError('sorce must between 0 and 100')
        
        self.sorce=value
        
s=Student()

 

s.set_sorce(1)

print(s.sorce)
        