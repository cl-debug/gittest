#coding=UTF-8
#多重继承
#动物类
class Animal(object):
    pass

class Mammal(Animal):
    pass

class Runnable(object):
    def run(self):
        print('Running...')
        
class Flyable(object):
    def fly(self):
        print('Flying...')        
        
        
class Dog(Mammal, Runnable):
    pass


class Bat(Mammal, Flyable):
    pass        