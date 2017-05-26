#coding=UTF-8
class Student(object):
    @property
    def birth(self):
        return self._birth
    
    @birth.setter
    def brth(self,value):
        self.__birth=value
        
    @property
    def age(self):
        return 2014 - self._birth
            
        