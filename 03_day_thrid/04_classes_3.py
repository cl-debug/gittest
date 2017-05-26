#coding=UTF-8

#利用完全动态的__getattr__，我们可以写出一个链式调用

class Chain(object):
    def __init__(self,path=''):
        self.__path=path
        
    def __getattr__(self,path):
        return Chain("%s%s" %(self.__path,path))
    
    def __str__(self):
        return self.__path
    
    
            