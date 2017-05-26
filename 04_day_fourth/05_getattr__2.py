#coding=UTF-8
#api链式调用
class Chain(object):
    
    def __init__(self,path=''):
        self.__path=path
        
    def __getattr__(self,path):
        return Chain('%s/%s'%(self.__path,path))
    
    def __str__(self):
        return self.__path
    
    __repr__=__str__
    
print Chain().name.gae.cc.cc.cc